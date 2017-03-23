from django.shortcuts import render
import urllib

# Create your views here.
def index (request):
    return render(request, 'personal/home.html')

def contact (request):
    return render(request,'personal/basic.html', {'content':[urllib.request.urlopen("https://api.spotify.com/v1/tracks/5KHxaN8OtPRuaxNqdVYH9j").read()]})