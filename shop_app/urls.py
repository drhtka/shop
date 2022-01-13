# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.urls import path, re_path
# from django.conf.urls import include, url
from shop_app import views
from accounts. views import authorization
#from .views import index
#from .views import contacts
from shop_app.views import ProdsListView

urlpatterns = [
    path(r'', views.index, name='index'),
    #path('shop/', index),
    path('contacts/', views.contacts,  name='contacts'),
    path('gallery/', views.gallery, name='gallery'),
    path('goods/', views.goods, name='goods'),
    path('category/', views.category, name='category'),
    # path('show/', views.show, name='show'),
    path('show/<int:pk>/', views.show, name='show'),
    path('shop_billing/', views.shop_billing, name='shop_billing'),
    path('shop_cart/', views.shop_cart, name='shop_cart'),
    path('shop_bay/', views.shop_bay, name='shop_bay'),
    path('final_order/', views.finalOrder, name='final_order'),
    path('dell_goods/', views.dell_goods, name='dell_goods'),
    path('shop_orders/', views.shop_orders, name='shop_orders'),
    path('send_order/', views.send_order, name='send_order'),
    path('sort_goods_categ/', views.sort_goods_categ, name='sort_goods_categ'),
    path('final_thanks/', views.final_thanks, name='final_thanks'),
    path('fetch_price/', views.fetch_price, name='fetch_price'),
    path('fetch_category/', views.fetch_category, name='fetch_category'),
    path('fetch_price_index/', views.fetch_price_index, name='fetch_pric_indexe'),
    path('fetch_category_index/', views.fetch_category_index, name='fetch_category_index'),
    path('priceIndexSort/', views.priceIndexSort, name='priceIndexSort'),
    path('authorization/', authorization, name='authorization'),
    # path('lk/', LKViews.lk, name='lk')

    path('lk_list/', ProdsListView.as_view(), name='lk_list'),
    path('lk/<int:pk>/', views.lk_detail, name='lk'),
    # path('lk/', views.lk_detail, name='lk'),



]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)