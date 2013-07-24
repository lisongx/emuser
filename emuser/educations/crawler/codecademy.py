import requests
import lxml.html.soupparser as htmltree


class CodecademyClient(object):

    BEFORE_LOGIN_TOKEN_URL = "http://www.codecademy.com/zh/sign_in"
    BEFORE_LOGIN_TOKEN_XPATH = ("//*[@id='new-session']/div[1]"
                                "/input[@name='authenticity_token']"
                                "/@value")

    def __init__(self):
        self.client = requests.session()

    def fetch_login_token(self):
        response = self.client.get(self.BEFORE_LOGIN_TOKEN_URL)
        response.raise_for_status()
        tree = htmltree.fromstring(response.text)
        token = tree.xpath(self.BEFORE_LOGIN_TOKEN_XPATH)[0]
        return token
