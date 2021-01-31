# -*- coding: utf-8 -*-
"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
#from rest_framework.urlpatterns import format_suffix_patterns
#from rest_framework.views import APIView
#from rest_framework.viewsets import ModelViewSet
#from blog.api import views as api_views
#from blog.api.serializers import CommentSerializer
from django.conf import settings
from django.conf.urls.static import static

from accounts import views
from api import views as api_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('allauth.urls')),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/', views.accounts, name='accounts'),
    path('fastregister/', views.fastregister, name='fastregister'),


    path('', include('shop_app.urls')),
    path('articles', include('articles.urls')),
    path('test/', include('test_url.urls')),
    #path('blog/', include('blog.urls')),
    path("api/",
        api_views.GoodsListView.as_view(),
        name="api_list"),
    path("api/<int:id>",
        api_views.GoodsListDitailView.as_view(),
        name="api_goods_list"),

    path("api/category",
       api_views.CategoryListView.as_view(),
       name="category_list"),

    #path("api/posts/<pk>",
    #     api_views.CommentDetailView.as_view(),
    #     name="api_post_detail"),
    #path('api/post-detail/<int:pk>',
    #     api_views.PostListUrlView.as_view()),
    #re_path("api/my_posts/(?P<title>\D+)/", api_views.PostListUrlView.as_view(), name="api_post_list"),
    #re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)/', views.users),
    #re_path("api/posts/<blogpost>[^/]", api_views.PostListUrlView.as_view(), name="api_post_list"),
    #path("api/posts/<str:blogpost>/", api_views.PostListUrlView.as_view(), name="api_post_list"),
    #re_path("api/posts/<blogpost>[^/]+/comments/", api_views.PostListUrlView.as_view(), name="api_post_list"),
    #url(r'^(?P<blogpost>[^/]+)/comments/(?P<id>[^/]+)/$', ModelViewSet.as_view(resource=CommentSerializer)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#<str:title>/