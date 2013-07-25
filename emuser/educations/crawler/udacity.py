import random

import requests


class UdacityClient(object):

    LOGIN_URL = "https://udacity.com/api/session"
    LOGIN_REFERER_URL = "https://www.udacity.com"

    LIST_URL = ""
    
    def __init__(self):
        self.client = requests.session()

    @property
    def xsrf_token(self):
        return self.client.cookies["XSRF-TOKEN"]

    @xsrf_token.setter
    def xsrf_token(self, value):
        self.client.cookies["XSRF-TOKEN"] = value

    def login(self, email, password):
        self.client.get(self.LOGIN_REFERER_URL, verify=False)
        headers = {"Referer": self.LOGIN_REFERER_URL,
                   "X-Requested-With": "XMLHttpRequest",
                   "X-XSRFToken": self.xsrf_token}
        data = {'udacity':{"email": email, "password": password}}

        response = self.client.post(self.LOGIN_URL, data=data, headers=headers,
                verify=False)
        response.raise_for_status()
        return response.ok

    def fetch_list(self):
        pass

if __name__ == '__main__':
    client = UdacityClient()
    print client.login('','')
