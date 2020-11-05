# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# Create your models here.
# from django.apps import apps
# apps.get_models()
# from django.db.models.signals import pre_delete
# from django.dispatch.dispatcher import receiver
# import os
# from django.db.models.signals import pre_delete, post_delete
# from django.dispatch.dispatcher import receiver
#
# from shop import settings




class CategoryModel(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'category'

    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    catname = models.CharField('название', max_length=15, blank=True)
    description = models.TextField('Описание', blank=True, null=True)
    img_categ = models.ImageField(upload_to='img_categ', verbose_name='Изображение категории', blank=True, null=True)

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

class Image(models.Model):
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        db_table = 'photos'

    image = models.ImageField('фото', upload_to="img", )
    content_type = models.ForeignKey(ContentType, default=None, related_name='images', on_delete=models.CASCADE)
    # goods = models.ForeignKey(GoodsModel, on_delete=models.CASCADE, related_name='orders')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    # def clean(self, exclude=None):
    #     pass

class GoodsModel(models.Model):
    class Meta:
        verbose_name = 'Тоовар'
        verbose_name_plural = 'Товары'
        db_table = 'goods'

    others = '0'
    clothes = '1'
    apparature = '2'
    books = '3'

    CATEGORY_CHOICES = (
        (others, 'Разное'),
        (clothes, 'Одежда'),
        (apparature, 'Аппаратура'),
        (books,'Книги'),
    )

    id = models.AutoField(primary_key=True, auto_created=True, null=False)
    goodsname = models.CharField('Название', max_length=20, blank=True, null=True)
    category = models.CharField('Категории', max_length=15, null=True, choices=CATEGORY_CHOICES)
    price = models.CharField(max_length=30, verbose_name='Цена', blank=True)
    img = models.ImageField(upload_to='img', verbose_name='Основное изображение', blank=True, null=True)
    desc = models.TextField('Описание', blank=True, null=True)
    tags = GenericRelation(Image)

    def publich(self):
        self.order_date = timezone.now()
        self.save()

    def __str__(self):
        return self.goodsname

class Product(models.Model):
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереи'
        db_table = 'product'

    name = models.CharField('Галерея', max_length=100)
    #tags = GenericRelation(Image)

    def __str__(self):
        return self.name

# from django.db.models import ProtectedError, signals
#
#
# @receiver(signals.pre_delete, Image)
# def protect_delete(sender, instance, **kwargs):
#     if instance.image.exists():
#         raise ProtectedError()

    # def delete(self):
    #     images = Image.objects.filter(content_type=self)
    #     if images:
    #         for image in images:
    #             image.delete()
    #     super(Product, self).delete()



# @receiver(pre_delete, sender=Image)
# def delete_image(sender, instance, **kwargs):
#     # Pass false so FileField doesn't save the model.
#     if instance.image:
#         instance.image.delete(True)

# from django.db.models.signals import pre_delete
# from django.dispatch.dispatcher import receiver
#
# @receiver(pre_delete, sender=Image)
# def image_delete(sender, instance, **kwargs):
#     # Pass false so FileField doesn't save the model.
#     instance.file.delete(False)


# def _delete_file(path):
# Deletes file from filesystem.
# if os.path.isfile(path):
#     os.remove(path)
#
# @receiver(models.signals.post_delete, sender=Image)
# def delete_img_post_delete_post(sender, instance, *args, **kwargs):
#     if instance.image:
#         _delete_file(instance.image.path)
# if instance.content_type:
#     _delete_file(instance.content_type.path)
# if instance.object_id:
#     _delete_file(instance.object_id.path)
# if instance.content_object:
#     _delete_file(instance.content_object.path)


# def delete(self, *args, **kwargs):
#     os.rmdir(os.path.join(settings.MEDIA_ROOT, self.image))
#     super(Image, self).delete(*args, **kwargs)

# print('mayak')
# print(object_id, image.)
# def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#     self._image = self.image
#
# def save(self, *args, **kwargs):
#     if self.image != self._image:
#         self._image.delete()
#         super().save(*args, **kwargs)
