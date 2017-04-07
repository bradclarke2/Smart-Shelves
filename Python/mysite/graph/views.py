from django.shortcuts import render
from django.http import HttpResponse
import urllib

# Create your views here.
def index(request):
    try:
        content = urllib.request.urlopen("http://127.0.0.1:5000/stock/").read()
    except urllib.error.HTTPError as err:
        if err.code == 500:
            content = "not found"
            print ("Page not found!")
        elif err.code == 403:
            print ("Access denied!")
        else:
            print ("Something happened! Error code", err.code)
    except urllib.error.URLError as err:
        print ("Some other error happened:", err.reason)
    
    return render(request,'personal/test.html',{'stock':content})