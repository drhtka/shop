# Generated by Django 2.2 on 2020-10-21 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0014_auto_20201018_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='img_categ',
            field=models.ImageField(blank=True, null=True, upload_to='img_categ', verbose_name='Изображение категории'),
        ),
    ]
