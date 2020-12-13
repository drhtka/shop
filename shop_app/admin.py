# -*- coding: utf-8 -*-
from django.contrib import admin
from shop_app.models import GoodsModel, CategoryModel, BillingModel, OrdersModel, Image, Product
from django.contrib.contenttypes.admin import GenericTabularInline#, GenericInlineModelAdmin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('catname', 'id',)
    list_filter = ('catname', 'id',)

class BillngAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'bill_id')
    list_filter = ('id', 'bill_id')

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

admin.site.register(GoodsModel, GoodsAdmin,)
admin.site.register(CategoryModel, CategoryAdmin,)
admin.site.register(BillingModel, BillngAdmin,)
admin.site.register(OrdersModel, OrdersAdmin,)
admin.site.register(Product, ProductAdmin)