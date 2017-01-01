from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.posts_home),
    url(r'^(?P<id>\d+)/$', views.posts_detail),
]
