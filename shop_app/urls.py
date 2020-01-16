# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path, re_path

from shop_app import views
#from .views import index
#from .views import contacts

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    #path('shop/', index),
    path('contacts/', views.contacts),
    path('gallery/', views.gallery),
    path('goods/', views.goods),
    path('category/', views.category),
    path('show/', views.show),
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)