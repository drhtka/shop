# Generated by Django 2.2 on 2020-10-22 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0015_categorymodel_img_categ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsmodel',
            name='catid',
            field=models.CharField(choices=[('0', 'Разное'), ('1', 'Одежда'), ('2', 'Аппаратура'), ('3', 'Книги')], max_length=15, null=True, verbose_name='Категории'),
        ),
    ]
