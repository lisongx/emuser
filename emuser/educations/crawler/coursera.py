import random

import requests
import dateutil.parser


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

    def _fetch_list(self):
        response = self.client.get(self.LIST_URL)
        response.raise_for_status()
        return response.json()

    def yield_normalized_courses(self):
        for course_record in self._fetch_list():
            grades_release_date = self._find_grades_release_date(course_record)
            if not grades_release_date or not course_record["display"]:
                continue

            course_home_templ = "https://www.coursera.org/course/%s"

            normalized_item = dict(
                subject=course_record["name"],
                source="coursera",
                url=course_home_templ % course_record["short_name"],
                picture_url=course_record["photo"],
                datetime=grades_release_date,
            )
            yield normalized_item

    def _find_grades_release_date(self, course_record):
        release_dates = [dateutil.parser.parse(course["grades_release_date"])
                         for course in course_record["courses"]
                         if course["grades_release_date"]]
        if release_dates:
            return max(release_dates)
