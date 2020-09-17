# -*- coding: utf-8 -*-
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
    catid = models.CharField('id категории', max_length=15, blank=True)
    price = models.CharField(max_length=30, verbose_name='Цена', blank=True)
    img = models.ImageField(upload_to='img', verbose_name='Основное изображение', blank=True, null=True)
    desc = models.TextField('Описание', blank=True, null=True)

    def publich(self):
        self.order_date = timezone.now()
        self.save()

    def __str__(self):
        return self.goodsname