from django.conf import settings
# from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Article(models.Model):
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        db_table = 'articles'
        # ordering = ('pk')

    title = models.CharField('Заголовок', max_length=255)
    body = models.TextField('Текст')
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField('Автор', max_length=50)
    img = models.ImageField(upload_to='img', verbose_name='Основное изображение')

    def publich(self):
        self.order_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
