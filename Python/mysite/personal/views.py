from django.shortcuts import render
import numpy as np
from ast import literal_eval as ast
from django.template.context_processors import request
import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
from . import test2 as key

# Create your views here.
def index (request):
    try:
        content = urllib.request.urlopen("http://127.0.0.1:5000/list/").read().decode('utf-8')
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
    
#     test = content.split('], [')
#     test = np.asarray(content)
    test = ast(content)
    counter = 0
    
    APIkey = key.api
    
    for c in test:
        b = c[0]
        headers = {
            # Request headers
            'Ocp-Apim-Subscription-Key': APIkey,
        }
        
        params = urllib.parse.urlencode({
            # Request parameters
            'gtin': b,
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
            c[4] = description
            g = b[-3:]
            c.append(g)
        except Exception as e:
            print("[Errno {0}] {1}".format(e.errno, e.strerror))
        
        counter = counter + 1 
        
                
    a = render(request,'personal/basic.html', {'content':test,#[urllib.request.urlopen("http://127.0.0.1:5000/measurements/").read()], 
#                                                'shelflocation':[urllib.request.urlopen("http://127.0.0.1:5000/shelflocation/").read()],
#                                                'pictureregen':urllib.request.urlopen("http://127.0.0.1:5000/pictureregen/")
                                               })
    return a
