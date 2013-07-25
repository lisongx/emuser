#-*- coding:utf-8 -*-

import datetime

from parsedatetime.parsedatetime import Calendar, Constants


def datetime_from_friendly_text(text, locale=None):
    #: FIXME ugly hack
    #: WTF!!! parsedatetime is full of bugs.
    if locale == "zh_CN":
        text = text.replace(u"个月", "months")\
                   .replace(u"月", "months")

    calendar = Calendar(Constants(localeID=locale))
    time_struct = calendar.parse(text)
    return datetime.datetime(*time_struct[0][:6])
