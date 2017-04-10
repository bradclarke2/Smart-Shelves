from django.shortcuts import render
from django.http import HttpResponse
from ast import literal_eval as ast
import urllib
import json
import http.client, urllib.request, urllib.parse, urllib.error, base64
from . import test2 as key

# Create your views here.
def index(request):
    try:
        content = urllib.request.urlopen("http://127.0.0.1:5000/stock/").read().decode('utf-8')
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
    APIkey = key.api
    
    for c in test:
        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': APIkey,
        }
        
        params = urllib.parse.urlencode({
            # Request parameters
            'gtin': c[1],
        })
        
        try:
            conn = http.client.HTTPSConnection('dev.tescolabs.com')
            conn.request("GET", "/product/?%s" % params, "{body}", headers)
            response = conn.getresponse()
            data = response.read()
            print(data)
            conn.close()
            parsed_data = json.loads(data)
            description = parsed_data['products'][0]['description']
            c.append(description)
            g = c[1]
            g = g[-3:]
            c.append(g)
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
    
     
        
    return render(request,'personal/test.html',{'stock':test, 
                                                'item':c})