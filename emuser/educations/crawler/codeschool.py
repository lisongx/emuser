#-*- coding: utf-8 -*-

import requests
import dateutil.parser
from lxml import etree


class CodeSchoolClient(object):
    CODESCHOOL_HOME_URL = 'https://www.codeschool.com'
    CODESCHOOL_LOGIN_URL = 'http://www.codeschool.com/users/sign_in'
    CODESCHOOL_COURSE_URL = 'http://www.codeschool.com/users/%s'

    def __init__(self):
        self.client = requests.session()

    @property
    def authenticity_token(self):
        response = self.client.get(self.CODESCHOOL_LOGIN_URL, verify=False)
        tree = etree.HTML(response.text)
        nodes = tree.xpath("//input[@name='authenticity_token']")
        if len(nodes)>0:
            authenticity_token = nodes[0].get('value')
            return authenticity_token
        raise Exception("authenticity_token not found!")

    def login(self, username, password):
        post_data = {
            'return': '/',
            'utf8': u'✓',
            'authenticity_token': self.authenticity_token,
            'user[login]': username,
            'user[password]': password,
        }
        response = self.client.post(self.CODESCHOOL_LOGIN_URL, data=post_data, verify=False)
        response.raise_for_status()
        tree = etree.HTML(response.text)
        node = tree.xpath("/html/body/nav/div/ul/li[5]/a")[0]
        self.my_report_card_url = node.get("href")
        return response.ok

    def fetch_list(self):
        course_url = self.CODESCHOOL_HOME_URL + self.my_report_card_url
        response = self.client.get(course_url, verify=False)
        tree = etree.HTML(response.text)
        nodes = tree.xpath("/html/body/section/div/div[1]/ol/li")
        unfinished_nodes = tree.xpath("/html/body/section/div/div[2]/ol/li")
        nodes += unfinished_nodes
        return nodes

    def yield_normalized_courses(self):
        nodes = self.fetch_list()
        for n in nodes:
            img = n.xpath("./img")[0]
            a = n.xpath("./div/h3/a")[0]
            try:
                time = n.xpath("./div/p/time")[0]
                datetime = time.get("datetime")
            except IndexError:
                datetime = "1989/8/6"
            yield dict(
                source='codeschool',
                subject=img.get('alt'),
                url=a.get('href'),
                picture_url=img.get('src'),
                datetime=dateutil.parser.parse(datetime),
            )
