# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import generics
from blog.models import Post, Comment
from blog.api.serializers import PostSerializer, CommentSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentDetailView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

