# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.reverse import reverse

from shop_app.models import GoodsModel, CategoryModel




class GoodsModelSerializer(serializers.ModelSerializer):
        category_choices = serializers.CharField(source='get_category_display')
        class Meta:
                model = GoodsModel

                fields = ('id', 'goodsname', 'category', 'price', 'img', 'category_choices')
                ordering = ('id',)

class CategoryModelSerializer(serializers.ModelSerializer):
        class Meta:
                model = CategoryModel
                fields = ('id', 'catname', 'img_categ', 'cat_true')
                ordering = ('id',)

# class CommentSerializer(serializers.ModelSerializer):
#         class Meta:
#                 model = Comment
#                 fields = ('blogpost', 'comment', 'created',)
#                 ordering = ('-created',)

