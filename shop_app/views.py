# -*- coding: utf-8 -*-
from django.shortcuts import render
import psycopg2
from django.http import HttpResponse


def index(request):
    return render(request, 'shop_app/index.html')

def contacts(request):
    connection = psycopg2.connect(user="shopuser",
                                  password="shop_pos0701",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="shop_pos")
    cursor = connection.cursor() # переменной присваиваем доступ к базе метод cursor()
    postgreSQL_select_Query = "select * from pages where name = 'contacts'"

    cursor.execute(postgreSQL_select_Query) # сделать выборку execute через запрос (postgreSQL_select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    mobile_records = cursor.fetchall()  # fetchall выборка всего контента, fetchone выборка одного
    #print(mobile_records)
    #print("Print each row and it's columns values")
    #print(mobile_records)
    return render(request, 'shop_app/contacts.html', context={'contacts': 'hello', 'mobile_records': mobile_records})

def goods(request):
    print(123)
    #idcat = request.GET.get('i', default=None)
    connection = psycopg2.connect(user="shopuser",
                                  password="shop_pos0701",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="shop_pos")
    cursor = connection.cursor()
    if request.GET.get('i'):
        idcat = request.GET.get('i', default=None)
        postgreSQL_select_Query = "select * from goods where catid = " + idcat + " ORDER BY id ASC"
    else:
        postgreSQL_select_Query = "select * from goods ORDER BY id ASC"
    print(postgreSQL_select_Query)

    cursor.execute(postgreSQL_select_Query)
    goods = cursor.fetchall()
    print(goods)

    return render(request, 'shop_app/goods.html', context={'goods': goods})

def category(request):
    connection = psycopg2.connect(user="shopuser",
                                  password="shop_pos0701",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="shop_pos")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from category"

    cursor.execute(postgreSQL_select_Query)
    category = cursor.fetchall()

    return render(request, 'shop_app/category.html', context={'category': category})

def gallery(request):
    return render(request, 'shop_app/gallery.html')

def show(request):
#    idgoods = request.GET.get('i', default=None)
    connection = psycopg2.connect(user="shopuser",
                                  password="shop_pos0701",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="shop_pos")


    if request.GET.get('i'):
        idgoods = request.GET.get('i', default=None)
        postgreSQL_select_Query = "select * from goods where id = " + idgoods + " ORDER BY id ASC"
    else:
        postgreSQL_select_Query = "select * from goods ORDER BY id ASC"

    cursor = connection.cursor()
    cursor.execute(postgreSQL_select_Query)
    show = cursor.fetchall()


    return render(request, 'shop_app/showp.html', context={'show': show})

#"""#    postgreSQL_select_Query = "select * from goods where idgoods = " + idgoods + " ORDER BY id ASC"
#    postgreSQL_select_Query = "select * from goods ORDER BY id ASC" #where id = 1
#   postgreSQL_select_Query = "select * from goods where catid = " + idcat + " ORDER BY id ASC

#    show = cursor.fetchone()""""