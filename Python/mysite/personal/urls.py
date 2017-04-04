from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^webapp/', include('webapp.urls')),
    url(r'^graph/', include('graph.urls')),
#    url(r'^map/img/', views.mapping, name ='mapping'),
    url(r'^$', views.index, name='index'),
#     url(r'^contact/', views.contact, name='contact'),
]
