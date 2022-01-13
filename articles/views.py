# -*- coding: utf-8 -*-

from django.shortcuts import render
from .models import Article

from django.views.generic import ListView, DetailView


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

    def get(self, request):
        # render_session = []
        if request.session.get('my_list'):
            cart_seshion = request.session['my_list']
            count_render_session = len(cart_seshion)
            render_session = request.session['my_list']
            return render(request, 'article_list.html', {'count_render_session': count_render_session,
                                                         'render_session': render_session,})
        else:
            return render(request, 'article_list.html',)

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'