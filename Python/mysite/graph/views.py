from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'personal/test.html',{'welcome':HttpResponse("<h2>HEY!</h2>")})

def mapping(request):
    return render(request,'personal/map.html',{'welcome':HttpResponse("<h2>HEY!</h2>")})