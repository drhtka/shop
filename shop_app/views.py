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
    #print(postgreSQL_select_Query)

    cursor.execute(postgreSQL_select_Query)
    goods = cursor.fetchall()
    #print(goods)
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

def shop_billing(request):
    #id_shop_billing = request.POST.get('i', default=None)
    connection = psycopg2.connect(user="shopuser",
                                  password="shop_pos0701",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="shop_pos")

    id_shop_billing = request.GET.get('i', default=None)
    name = request.GET.get('name', default=None)
    price = request.GET.get('price', default=None)
    img = request.GET.get('img', default=None)
    #img = str(img)
    print(type(img))
    postgreSQL_select_Query = "INSERT INTO shop_billing (name, sum) VALUES ('" + name + "', '" + price + "')"
    print(postgreSQL_select_Query)
    cursor = connection.cursor()
    cursor.execute(postgreSQL_select_Query)
    connection.commit()

    postgreSQL_select_Query = "SELECT * FROM shop_billing ORDER BY id DESC LIMIT 1"# INSERT INTO shop_order (bill_id, tovar_name, price)
    cursor = connection.cursor()
    cursor.execute(postgreSQL_select_Query)
    show = cursor.fetchone()
    print(show[0])
    find_id = str(show[0])
    print(type(find_id))
    postgreSQL_select_Query_2 = "INSERT INTO shop_orders (bill_id, price, tovar_name, img) VALUES (" + find_id + ", '" + price + "', '" + name + "', '" + img + "')"
    print(postgreSQL_select_Query_2)

    cursor = connection.cursor()
    cursor.execute(postgreSQL_select_Query_2)
    connection.commit()
    # sission внести имя name
    #request.session.modified = True
    request.session['name'] = name

    #name2 = request.session.get('name')
    #request.session['price']= price
    #name3 = request.session.get('price')

    #print(request.session['name']), 'name3': name3
    return render(request, 'shop_app/shop_billing.html', {'name': name})

#    find_id = int(find_id)
#    postgreSQL_select_Query_1 = "INSERT INTO shop_orders (bill_id, tovar_name, price, img) VALUES (" + find_id + ", '" + name + "', '" + price + "', '" + img + "')"
#    print(postgreSQL_select_Query_1)

    #return render(request, 'shop_app/shop_billing.html',)





 #   id_shop_billing = request.GET.get('i', default=None)
 #   name = request.GET.get('name', default=None)
 #   price = request.GET.get('price', default=None)
 #   postgreSQL_select_Query = "INSERT INTO shop_orders (bill_id, tovar_name, price) VALUES ('" + name + "', '" + sum + "')"
