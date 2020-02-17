# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.reverse import reverse

from blog.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
        class Meta:
                model = Post
                fields = ('title', 'text', 'created_date', 'published_date',)
                ordering = ('-created_date',)


class CommentSerializer(serializers.ModelSerializer):
        class Meta:
                model = Comment
                fields = ('blogpost', 'comment', 'created',)
                ordering = ('-created',)

""" def comments(self, instance):
return reverse('comments', kwargs={'blogpost':instance.id})                
def blogpost(self, instance):
return reverse('blog-post', kwargs={'id':instance.blogpost.id})"""
