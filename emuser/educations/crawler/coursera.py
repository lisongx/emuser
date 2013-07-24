import random

import requests


chars = lambda from_, to: [chr(n) for n in range(ord(from_), ord(to) + 1)]


class CourseraClient(object):

    LOGIN_URL = "https://accounts.coursera.org/api/v1/login"
    LOGIN_REFERER_URL = "https://accounts.coursera.org/signin"

    CSRF_TOKEN_CHARS = chars('0', '9') + chars('a', 'z') + chars('A', 'Z')

    LIST_URL = "https://www.coursera.org/maestro/api/topic/list_my"

    def __init__(self):
        self.client = requests.session()
        self.csrf_token = "".join(random.sample(self.CSRF_TOKEN_CHARS, 24))

    @property
    def csrf_token(self):
        return self.client.cookies["csrftoken"]

    @csrf_token.setter
    def csrf_token(self, value):
        self.client.cookies["csrftoken"] = value

    def login(self, email, password):
        headers = {"Referer": self.LOGIN_REFERER_URL,
                   "X-Requested-With": "XMLHttpRequest",
                   "X-CSRFToken": self.csrf_token}
        data = {"email": email, "password": password}

        response = self.client.post(self.LOGIN_URL, data=data, headers=headers)
        response.raise_for_status()
        return response.ok

    def fetch_list(self):
        response = self.client.get(self.LIST_URL)
        response.raise_for_status()
        return response.json()
