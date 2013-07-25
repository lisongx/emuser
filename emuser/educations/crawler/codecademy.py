import re

import requests
import lxml.html.soupparser as htmltree

from emuser.educations.helpers import datetime_from_friendly_text


class CodecademyClient(object):

    BEFORE_LOGIN_TOKEN_URL = "http://www.codecademy.com/zh/sign_in"
    BEFORE_LOGIN_TOKEN_XPATH = ("//*[@id='new-session']/div[1]"
                                "/input[@name='authenticity_token']"
                                "/@value")

    LOGIN_REFERER_URL = "http://www.codecademy.com/zh/sign_in"
    LOGIN_URL = "http://www.codecademy.com/zh/sign_in"

    HOME_URL = "http://www.codecademy.com/"
    PROFILE_XPATH = "//*[@id='header']/div[1]/nav[2]/ul/li[2]/a/@href"
    PROFILE_URL = "http://www.codecademy.com/%s"
    COURSES_XPATH = "//*[@id='wrapper']/div[2]/div/div[2]/div/div"
    SUBJECT_XPATH = "a/div[contains(@class, 'track-name')]/@title"
    STAT_XPATH = ("a/div[contains(@class, 'track-progress-stats')]/span"
                  "/span[contains(@class, 'stat-value')]/text()")

    def __init__(self):
        self.client = requests.session()

    def fetch_login_token(self):
        response = self.client.get(self.BEFORE_LOGIN_TOKEN_URL)
        response.raise_for_status()
        tree = htmltree.fromstring(response.text)
        token = tree.xpath(self.BEFORE_LOGIN_TOKEN_XPATH)[0]
        return token

    def login(self, email, password):
        headers = {"Referer": self.LOGIN_REFERER_URL}
        data = {"utf8": u'\u2713', "commit": u"\u767b\u9646",
                "authenticity_token": self.fetch_login_token(),
                "user[login]": email, "user[password]": password,
                "user[remember_me]": 1}

        response = self.client.post(self.LOGIN_URL, data=data, headers=headers)
        response.raise_for_status()
        return response

    def yield_normalized_courses(self):
        username = self._fetch_username()
        response = self.client.get(self.PROFILE_URL % username)
        response.raise_for_status()
        tree = htmltree.fromstring(response.text)
        for element in tree.xpath(self.COURSES_XPATH):
            try:
                percent = float(element.get("data-percent"))
            except ValueError:
                percent = 0.0
            if percent != 1.0:
                continue

            course_home = self._parse_home_link(element)
            subject = self._parse_subject(element)
            datetime = self._parse_datetime(element)
            picture_url = self._fetch_picture_url(course_home)

            yield dict(subject=subject, source="codecademy", url=course_home,
                       picture_url=picture_url, datetime=datetime)


    def _fetch_username(self):
        response = self.client.get(self.HOME_URL)
        tree = htmltree.fromstring(response.text)
        profile_url = tree.xpath(self.PROFILE_XPATH)[0]
        username = re.search(r"/users/([^/]+)", profile_url).group(1)
        return username

    def _fetch_picture_url(self, course_home):
        response = self.client.get(course_home)
        tree = htmltree.fromstring(response.text)
        return tree.xpath("//*[@id='curriculum']/div[4]/div[2]/img/@src")[0]

    def _parse_home_link(self, element):
        return self.HOME_URL + element.xpath("a/@href")[0].lstrip("/")

    def _parse_subject(self, element):
        return element.xpath(self.SUBJECT_XPATH)[0].strip()

    def _parse_datetime(self, element):
        plain_text = element.xpath(self.STAT_XPATH)[0]
        return datetime_from_friendly_text("%s ago" % plain_text)
