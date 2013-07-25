from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseBadRequest, HttpResponseRedirect, HttpResponse

from emuser.educations.crawler.coursera import CourseraClient
from record.models import Record
from django.utils import simplejson
from django.core import serializers

import collections
import json


def index(request):
    return render_to_response('index.html')

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

def resume(request, user_id):
    user_id=2
    records = Record.objects.filter(user=int(user_id)).all()
    data = serializers.serialize('json', records)
    data = json.loads(data)

    ret_dict = {}
    for d in data:
        ret_dict.setdefault(d['fields']['source'],[]).append(d['fields'])
        del ret_dict.setdefault(d['fields']['source'],[])[-1]['display']
    return HttpResponse('['+str(convert(ret_dict)).replace("'", '"')+']', mimetype='application/json')


@login_required
def courses(request):
    user = request.user
    coursera = user.records.filter(source='coursera')
    return render_to_response('courses.html',locals(),
            context_instance=RequestContext(request))

@login_required
def coursera(request):
    if request.POST:
        user = request.user
        username = request.POST.get('username')
        password = request.POST.get('password')
        client = CourseraClient()
        if client.login(username, password):
            courses = client.yield_normalized_courses()
            if courses:
                user.records.filter(source='coursera').delete()
                for course in courses:
                    Record.objects.create(user=user, **course)
                return HttpResponseRedirect('/courses/')

    return HttpResponseBadRequest()
