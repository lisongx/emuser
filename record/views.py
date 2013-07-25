from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseBadRequest, HttpResponseRedirect

from emuser.educations.crawler.coursera import CourseraClient
from record.models import Record

def index(request):
    return render_to_response('index.html')

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
        client.login(username, password)
        print "start fetch"
        courses = client.yield_normalized_courses()
        for course in courses:
            Record.objects.create(user=user, **course)
        return HttpResponseRedirect('/courses/')
    else:
        return HttpResponseBadRequest()
