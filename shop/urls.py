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
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

#from blog.api import views as api_views
#from blog.api.serializers import CommentSerializer



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop_app.urls')),
    path('test/', include('test_url.urls')),
    #path('blog/', include('blog.urls')),
    #path("api/posts/",
    #     api_views.PostListView.as_view(),
    #     name="api_post_list"),
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
]


#<str:title>/