# Generated by Django 2.2 on 2021-07-21 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_auto_20210721_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsmodel',
            name='price',
            field=models.IntegerField(blank=True, max_length=30, verbose_name='Цена'),
        ),
    ]
