# -*- coding: utf-8 -*-
from django.db.models import Q
from django.http import request, JsonResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer


from shop_app.models import GoodsModel, CategoryModel
from api.serializers import GoodsModelSerializer, CategoryModelSerializer

class GoodsListView(generics.ListAPIView):
    queryset = GoodsModel.objects.all()
    print('queryset')
    print(queryset)
    serializer_class = GoodsModelSerializer


class GoodsListDitailView(APIView):

    def post(self, request, id):
        posts = GoodsModel.objects.filter(id=id)
        serializer = GoodsModelSerializer(posts, many=True)
        # print(serializer.data)
        # print(serializer.data["slug"])
        return Response(serializer.data)

class CategoryListView(generics.ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategoryModelSerializer


###########
# class GoodsListView(generics.ListAPIView):
# class GoodsListView(generics.RetrieveAPIView):
#     queryset = GoodsModel.objects.all()
#     serializer_class = GoodsModelSerializer
#     # renderer_classes = [TemplateHTMLRenderer]
#     #
#     # def get(self, request, *args, **kwargs):
#     #     self.object = self.get_object()
#     #     return Response({'goods_api': self.object}, template_name='shop_app/big_retail/category.html')
#
# class GoodsListDitailView(APIView):
#
#     def get(self, request, id):
#         goodss = GoodsModel.objects.filter(id=id)
#         serializer = GoodsModelSerializer(goodss, many=True)
#         print(serializer.data)
#
#         return Response(serializer.data)
#         # if request.accepted_renderer.format == 'html':
#         #     data = serializer.data
#         #     # return render(request, 'shop_app/big_retail/shop-list.html', {'api': serializer.data})
#         #     return Response(data, template_name='shop_app/big_retail/shop-list.html')


