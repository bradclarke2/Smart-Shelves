from django.shortcuts import render
<<<<<<< HEAD
# from Main.main import testthepythonintegration
=======
import urllib
>>>>>>> 2c3ecc462cd14ed3532f9855d6268b8385dd181a

# Create your views here.
def index (request):
    a = render(request,'personal/basic.html', {'content':[urllib.request.urlopen("http://127.0.0.1:5000/measurements/").read()], 'shelflocation':[urllib.request.urlopen("http://127.0.0.1:5000/shelflocation/").read()]})
    return a