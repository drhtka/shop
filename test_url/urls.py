# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path, include, re_path
from test_url import views


urlpatterns = [

    re_path(r'^test_one/(d{1,2})/$', views.test_one),
    re_path(r'^test_two/$', views.test_two),
    re_path(r'^time/plus/\d+/', views.hours_ahead),
    #re_path(r'^products/\d+/', views.products),
    re_path(r'^products/(?P<productid>\d+)/', views.products),
    re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
]