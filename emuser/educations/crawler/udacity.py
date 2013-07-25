import random

import requests


<<<<<<< HEAD
chars = lambda from_, to: [chr(n) for n in range(ord(from_), ord(to) + 1)]


=======
>>>>>>> 17a528bfa3bc275c17f31596ae2a72e1b4473946
class UdacityClient(object):

    LOGIN_URL = "https://udacity.com/api/session"
    LOGIN_REFERER_URL = "https://www.udacity.com"

<<<<<<< HEAD

    LIST_URL = ""

=======
>>>>>>> 17a528bfa3bc275c17f31596ae2a72e1b4473946
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
<<<<<<< HEAD
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
    print client.login('shanzi@diumoo.net','find1way!')
=======

        headers = {"Referer": self.LOGIN_REFERER_URL,
                   "X-Requested-With": "XMLHttpRequest",
                   "X-XSRFToken": self.xsrf_token}
        data = {'udacity': {"email": email, "password": password}}

        response = self.client.post(self.LOGIN_URL, data=data, headers=headers,
                                    verify=False)
        response.raise_for_status()
        return response.ok
>>>>>>> 17a528bfa3bc275c17f31596ae2a72e1b4473946
