from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from graph.models import Post

urlpatterns = [ 
                url(r'^$', ListView.as_view(
                                    queryset=Post.objects.all().order_by("-date")[:25],
                                    template_name="blog/blog.html")),
            ]
