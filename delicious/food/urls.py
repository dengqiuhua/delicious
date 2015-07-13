# coding=utf-8
#Created by dengqiuhua on 15-7-12.
from django.conf.urls import patterns,include, url
from views import *

urlpatterns=patterns('',
    url(r'^$', Index.as_view(),name="food-index"),

)