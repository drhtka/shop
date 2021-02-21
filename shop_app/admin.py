# -*- coding: utf-8 -*-
from django.contrib import admin

from accounts.models import CustomUser
from shop_app.models import GoodsModel, CategoryModel, BillingModel, OrdersModel, Image, Product
from django.contrib.contenttypes.admin import GenericTabularInline#, GenericInlineModelAdmin
from django.contrib import admin
# from .models import *


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'lead', 'phone', 'email')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('catname', 'id', 'description', 'cat_true',)
    list_filter = ('catname', 'id',)

class BillngAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_cart', 'user_phone', 'created', 'sum', 'null_one')
    list_filter = ('user_cart',)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill_id', 'created', 'tovar_name', 'price', 'user_end')
    list_filter = ('created', 'user_end', 'price')

class ImageInline(GenericTabularInline):
    model = Image

    list_filter = ('object_id')
    list_display = ('object_id')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    inlines = [
        ImageInline,
    ]

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'goodsname', 'category', 'price')
    list_filter = ('id', 'goodsname', 'price')
    inlines = [
        ImageInline, # связываем галерею с товаром
    ]


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(GoodsModel, GoodsAdmin,)
admin.site.register(CategoryModel, CategoryAdmin,)
admin.site.register(BillingModel, BillngAdmin,)
admin.site.register(OrdersModel, OrdersAdmin,)
admin.site.register(Product, ProductAdmin)