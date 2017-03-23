from django.shortcuts import render
import urllib


# Create your views here.
def index (request):
    a = render(request,'personal/basic.html', {'content':[urllib.request.urlopen("http://127.0.0.1:5000/measurements/").read()], 
                                               'shelflocation':[urllib.request.urlopen("http://127.0.0.1:5000/shelflocation/").read()]
                                               })
    return a