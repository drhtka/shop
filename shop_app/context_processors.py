# -*- coding: utf-8 -*-
from shop_app.models import GoodsModel, Image
import random

def gallery_index_tmp(request):
    gallery_index = Image.objects.filter(object_id=16).values_list()
    gallery_index_tmp = random.sample(list(gallery_index), 16)
    return {'gallery_index_tmp': gallery_index_tmp} # of course some filter here