from django.conf.urls import url, include
from django.views.generic import ListView, DetailView

from graph import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    
#             url(r'^$', ListView.as_view(
#                                   queryset=Post.objects.all().order_by("-date")[:25],
#                                    template_name="blog/blog.html")),
            ]
