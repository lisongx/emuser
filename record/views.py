# Create your views here.
from record.models import Record
from django.utils import simplejson
from django.core import serializers
from django.http import HttpResponse
import collections
import json


#test_file = "./test_case.json"
#f = open(test_file,"r")
#f.readline
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
    return HttpResponse(str(convert(ret_dict)).replace("'", '"'), mimetype='application/json')


from django.shortcuts import render_to_response

def index(request):
    return render_to_response('index.html')
