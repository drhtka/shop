# Generated by Django 2.2 on 2021-07-21 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_auto_20210721_2158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsmodel',
            options={'ordering': ['price'], 'verbose_name': 'Тоовар', 'verbose_name_plural': 'Товары'},
        ),
    ]
