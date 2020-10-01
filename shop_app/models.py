# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
# Create your models here.

class GoodsModel(models.Model):

    class Meta:
        verbose_name = 'Тоовар'
        verbose_name_plural = 'Товары'
        db_table = 'goods'

    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    goodsname = models.CharField('Название', max_length=20, blank=True, null=True)
    catid = models.IntegerField('id категории', null=True)
    price = models.CharField(max_length=30, verbose_name='Цена', blank=True)
    img = models.ImageField(upload_to='img', verbose_name='Основное изображение', blank=True, null=True)
    desc = models.TextField('Описание', blank=True, null=True)

    def publich(self):
        self.order_date = timezone.now()
        self.save()

    def __str__(self):
        return self.goodsname

class CategoryModel(models.Model):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'category'

    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    catname = models.CharField('название', max_length=15, blank=True)
    description = models.TextField('Описание', blank=True, null=True)

    def publich(self):
        self.order_date = timezone.now()
        self.save()

    def __str__(self):
        return self.catname

class BillingModel(models.Model):

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
        db_table = 'shop_billing'

    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    name = models.CharField('название', max_length=30, blank=True)
    sum = models.TextField('Сумма', blank=True, null=True)

    def publich(self):
        self.order_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class OrdersModel(models.Model):

    class Meta:
        verbose_name = 'Покупка'
        verbose_name_plural = 'Покупки'
        db_table = 'shop_orders'

    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    bill_id = models.CharField('id покупки', max_length=30, blank=True)
    tovar_name = models.CharField('название', max_length=30, blank=True)
    price = models.CharField(max_length=30, verbose_name='Цена', blank=True)
    img = models.CharField(max_length=30, verbose_name='Цена', blank=True)

    def publich(self):
        self.order_date = timezone.now()
        self.save()

    def __str__(self):
        return self.tovar_name

from django.contrib.contenttypes.fields import GenericForeignKey


class Image(models.Model):
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        db_table = 'photos'

    image = models.ImageField(upload_to="img")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    #print('mayak')
    #print(object_id, image.)


class Product(models.Model):
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
        db_table = 'product'

    name = models.CharField('Галерея', max_length=100)

    def __str__(self):
        return self.name