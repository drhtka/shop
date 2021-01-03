# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.reverse import reverse

from shop_app.models import GoodsModel, CategoryModel




class GoodsModelSerializer(serializers.ModelSerializer):
        class Meta:
                model = GoodsModel
                fields = ('id', 'goodsname', 'category', 'price', 'img')
                ordering = ('id',)

class CategoryModelSerializer(serializers.ModelSerializer):
        class Meta:
                model = CategoryModel
                fields = ('id', 'catname', 'img_categ')
                ordering = ('id',)

# class CommentSerializer(serializers.ModelSerializer):
#         class Meta:
#                 model = Comment
#                 fields = ('blogpost', 'comment', 'created',)
#                 ordering = ('-created',)

