# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
import psycopg2
from django.http import HttpResponse
from django.template import loader, Context


def index(request):
    #главная
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
    # все товары
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
    # категории товаров
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
    # детальное описание товара
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
    # выбираем товар и отправляем в корзину
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
    request.session.get('my_list')
    if len(request.session['my_list']) > 0:
        request.session['my_list'].append([name, price, img])
    else:
        request.session['my_list'] = []
        request.session['my_list'].append([name, price, img])

    request.session.modified = True
    print(request.session['my_list'])
    return render(request, 'shop_app/shop_billing.html', context={'name': name, 'price': price, 'img': img, 'cart_seshion': request.session['my_list']})


def finalOrder(request):
    # товары в корзине
    connection = psycopg2.connect(user="shopuser",
                                  password="shop_pos0701",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="shop_pos")

    id_shop_billing = request.GET.get('i', default=None)
    name = request.GET.get('name', default=None)
    price = request.GET.get('price', default=None)
    img = request.GET.get('img', default=None)

    for final in request.session['my_list']:
        print(123)
        print(final)

        cursor = connection.cursor()
        my_price = final[1]
        my_name = final[0]
        my_img = final[2]

        postgreSQL_select_Query_3 = "INSERT INTO shop_orders (tovar_name, price, img) VALUES ('" + my_name + "', '" + my_price + "', '" + my_img + "' )"
        print(postgreSQL_select_Query_3)
        cursor.execute(postgreSQL_select_Query_3)
        connection.commit()
    request.session['my_list'] = []
    #del request.session['my_list']

    return render(request, 'shop_app/show.html')


def dell_goods(request):
    #удалить товар из корзины
    name_dell = request.GET.get('id', default=None)
    print(name_dell)
    i = 0
    for dell_godd in request.session['my_list']:
        if name_dell == dell_godd[0]:
            del request.session['my_list'][i]
            break
        else:
            i += 1


    print(request.session['my_list'])

    return render(request, 'shop_app/del_goods.html')



# print("INSERT INTO shop_orders (tovar_name, price, img, bill_id) VALUES ('" + my_price + "', '" + my_name + "', '" + my_img + "', " + find_id + " )")
# find_id = str(id_shop_billing)
# #final_order = cursor.fetchall()