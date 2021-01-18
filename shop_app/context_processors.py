# -*- coding: utf-8 -*-
from shop_app.models import GoodsModel, Image
import random

def gallery_index_tmp(request):
    # для вывода фото в базовый shop_app
    gallery_index = Image.objects.filter(object_id=16).values_list()
    gallery_index_tmp = random.sample(list(gallery_index), 16)
    return {'gallery_index_tmp': gallery_index_tmp} # of course some filter here

#http://127.0.0.1:8800/media/
def media_url_cart(request):
    # для вывода фото в корзине при покупке с любого шаблона
    media_url_cart = 'http://127.0.0.1:8800/media/'
    return {'media_url_cart': media_url_cart}