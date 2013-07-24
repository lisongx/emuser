import requests
import lxml.html.soupparser as htmltree


class CodecademyClient(object):

    BEFORE_LOGIN_TOKEN_URL = "http://www.codecademy.com/zh/sign_in"
    BEFORE_LOGIN_TOKEN_XPATH = ("//*[@id='new-session']/div[1]"
                                "/input[@name='authenticity_token']"
                                "/@value")

    LOGIN_REFERER_URL = "http://www.codecademy.com/zh/sign_in"
    LOGIN_URL = "http://www.codecademy.com/zh/sign_in"

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
