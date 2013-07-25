# Create your views here.
from django.shortcuts import render_to_response

def index(request):
    if request.user.is_authenticated():
        return render_to_response('manage.html')
    return render_to_response('index.html')
