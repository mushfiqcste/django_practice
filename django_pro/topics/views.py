# Create your views here.
from django.http import HttpResponse
#my custom methods

def index(request):
	return HttpResponse("Hi Mushfiq")
