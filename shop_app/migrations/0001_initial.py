# Generated by Django 2.2 on 2021-07-21 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id заказа')),
                ('sum', models.CharField(blank=True, max_length=30, null=True, verbose_name='Сумма')),
                ('created', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата создания')),
                ('user_cart', models.CharField(blank=True, max_length=30, null=True, verbose_name='Покупатель в корзине')),
                ('user_phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Телефон покупателя')),
                ('null_one', models.IntegerField(default='0', max_length=2, verbose_name='Ноль или один')),
            ],
            options={
                'verbose_name': 'Товар в корзине перед подтверждением',
                'verbose_name_plural': 'Товары в корзине перед подтверждением',
                'db_table': 'shop_billing',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('catname', models.CharField(blank=True, max_length=15, verbose_name='название')),
                ('description', models.TextField(blank=True, default='0', verbose_name='Описание')),
                ('img_categ', models.ImageField(blank=True, null=True, upload_to='img_categ', verbose_name='Изображение категории')),
                ('cat_true', models.PositiveIntegerField(null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='GoodsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('goodsname', models.CharField(blank=True, max_length=20, null=True, verbose_name='Название')),
                ('category', models.CharField(choices=[('1', 'Одежда'), ('2', 'Аппаратура'), ('3', 'Книги'), ('4', 'Разное')], max_length=15, null=True, verbose_name='Категории')),
                ('price', models.CharField(blank=True, max_length=30, verbose_name='Цена')),
                ('img', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='Основное изображение')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Тоовар',
                'verbose_name_plural': 'Товары',
                'db_table': 'goods',
                'ordering': ['price'],
            },
        ),
        migrations.CreateModel(
            name='OrdersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('bill_id', models.CharField(blank=True, max_length=30, verbose_name='id заказа')),
                ('tovar_name', models.CharField(blank=True, max_length=150, verbose_name='название')),
                ('price', models.CharField(blank=True, max_length=30, verbose_name='Цена')),
                ('img', models.CharField(blank=True, max_length=150, verbose_name='Фото')),
                ('created', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата создания')),
                ('user_end', models.CharField(blank=True, max_length=30, null=True, verbose_name='Покупатель подтвердил')),
            ],
            options={
                'verbose_name': 'Подтвержденные товары',
                'verbose_name_plural': 'Подтвержденные',
                'db_table': 'shop_orders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Галерея')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галереи',
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img', verbose_name='фото')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
                'db_table': 'photos',
            },
        ),
    ]
