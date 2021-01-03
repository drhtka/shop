# -*- coding: utf-8 -*-
from articles.models import *


def object_list(request):
    object_list = Article.objects.all()
    # gallery_index_tmp = random.sample(list(gallery_index), 16)
    return {'object_list': object_list} # of course some filter here