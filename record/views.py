# Create your views here.
from record.models import Record
from django.utils import simplejson


#test_file = "./test_case.json"
#f = open(test_file,"r")
#f.readline
def resume(request, user_id=2):
    print data
    data = Record.objects.get(user=int(user_id)) 
    #= serializers.serialize('json', foos)

