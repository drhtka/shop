# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField('Телефон', max_length=12)
    lead = models.CharField('Лид', max_length=12, default=0, help_text='0 постоянный покупатель, 1 лид')

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
        db_table = 'costumers'

    def __str__(self):
        return self.phone
