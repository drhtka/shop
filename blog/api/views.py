# -*- coding: utf-8 -*-
from django.db.models import Q
from django.http import request
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Post, Comment
from blog.api.serializers import PostSerializer, CommentSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentDetailView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PostListUrlView(APIView):
    #queryset = Post.objects.filter(title='first news')

    def get(self, request, pk):
        posts = Post.objects.filter(id=pk)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

        #blogpost = Comment.objects.all()
        #blogposts = Comment.objects.filter(Q(creater=request.blogpost) | Q(invited=request.blogpost))
        #print(blogposts)
        #title = Comment.objects.filter(blogpost=blogpost)
        #print(title)
        #serializer = CommentSerializer(blogposts, many=True)
        #return Response({"data": serializer.data})


        #title = request.GET.get(title)
        #bg = Post.objects.filter(title=title)
        #serializer = PostSerializer(bg, many=True)
        #return Response({"data": serializer.data})


    #def __init__(self, required, name):
    #    print(name)
    #print(request.GET.get('i', default=None))

    #print(request.GET.get("name", default=None))
    # queryset = Post.objects.filter(title='first news')
    # serializer_class = PostSerializer

#get(username='ola')
