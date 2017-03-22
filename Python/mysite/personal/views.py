from django.shortcuts import render
# from Main.main import testthepythonintegration

# Create your views here.
def index (request):
    return render(request, 'personal/home.html')

def contact (request):
    return render(request,'personal/basic.html', {'content':['if you want this','do this']})
