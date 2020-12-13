# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.reverse import reverse

from shop_app.models import GoodsModel




class GoodsModelSerializer(serializers.ModelSerializer):
        class Meta:
                model = GoodsModel
                fields = ('id', 'goodsname', 'category', 'price',)
                ordering = ('id',)


# class CommentSerializer(serializers.ModelSerializer):
#         class Meta:
#                 model = Comment
#                 fields = ('blogpost', 'comment', 'created',)
#                 ordering = ('-created',)

