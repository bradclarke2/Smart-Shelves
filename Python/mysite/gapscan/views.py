from django.shortcuts import render
from django.http import HttpResponse
import http.client, urllib
from ast import literal_eval as ast

# Create your views here.
def index(request):
    try:
        content = urllib.request.urlopen("http://127.0.0.1:5000/gap/").read().decode('utf-8')
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
    
    test = ast(content)
    
    return render(request,'personal/gap.html',{'gap':test})

