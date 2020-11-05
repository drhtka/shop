# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path, re_path

from shop_app import views
#from .views import index
#from .views import contacts

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    #path('shop/', index),
    path('contacts/', views.contacts,  name='contacts'),
    path('gallery/', views.gallery, name='gallery'),
    path('goods/', views.goods, name='goods'),
    path('category/', views.category, name='category'),
    path('show/', views.show, name='show'),
    path('shop_billing/', views.shop_billing, name='shop_billing'),
    path('final_order/', views.finalOrder, name='final_order'),
    path('dell_goods/', views.dell_goods, name='dell_goods'),
    path('shop_orders/', views.shop_orders, name='shop_orders'),
    path('send_order/', views.send_order, name='send_order'),
    path('sort_goods_categ/', views.sort_goods_categ, name='sort_goods_categ'),
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)