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
    path('shop_billing/', views.shop_billing),
    path('final_order/', views.finalOrder),
    path('dell_goods/', views.dell_goods),
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)