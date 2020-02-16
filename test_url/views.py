# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render

def test_one(request):
    return render(request, 'test_url/test_one.html')

def test_two(request):
    return render(request, 'test_url/test_two.html')

def hours_ahead(request):
    return render(request, 'test_url/hours.html')

def products(request, productid):
    print(productid)
    print(request)
    prod = productid
    return render(request, 'test_url/prod.html', {'prod': prod})

def users(request, id, name):
    id = id
    name = name
    return render(request, 'test_url/users.html', {'id': id, 'name': name})