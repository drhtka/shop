# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
import psycopg2
from django.http import HttpResponse
from django.template import loader, Context
from shop_app.models import GoodsModel

def index(request):
    #главная
    all_goods = GoodsModel.objects.values_list()
    print('all_goods')
    print(all_goods)
    return render(request, 'shop_app/index.html', {'all_goods': all_goods})

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
    #idgoods = request.GET.get('i', default=None)
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
    #request.session['test'] = 123
    #print(request.session['test'])
    #request.session['my_list'] = []
    #request.session.get('my_list')
    test_ashow = show[0][1]
    chek_good = ''
    if request.session.get('my_list', True):
        show_get = request.session['my_list']
        for ts in show_get:
            if ts[0] == test_ashow:
                chek_good = 'disabled'
                break

    print(request.session['my_list'])
    return render(request, 'shop_app/showp.html', context={'show': show, 'chek_good': chek_good})

def shop_billing(request):
    #выбираем товар и отправляем в корзину
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

    if len(request.session['my_list']) > 0:
        print(request.session['my_list'])
        search_find_id = request.session['my_list'][0][3]
        request.session['my_list'].append([name, price, img, search_find_id])
    else:
        request.session['my_list'] = []
        postgreSQL_select_Query = "INSERT INTO shop_billing (name, sum) VALUES ('" + name + "', '" + price + "')"
        #вставляем запись в таблицу shop_billing - эта запись будет номером корзинки 26 min
        print(postgreSQL_select_Query)
        cursor = connection.cursor()
        cursor.execute(postgreSQL_select_Query)
        connection.commit()

        postgreSQL_select_Query = "SELECT * FROM shop_billing ORDER BY id DESC LIMIT 1"
        # после вставки получаем номер этой записи (номер корзинки)
        cursor = connection.cursor()
        cursor.execute(postgreSQL_select_Query)
        show = cursor.fetchone()
        print(show[0])
        find_id = str(show[0])
        print(type(find_id))

        request.session['my_list'].append([name, price, img, find_id])

    request.session.modified = True
    print(request.session['my_list'])
    return render(request, 'shop_app/shop_billing.html', context={'name': name, 'price': price, 'img': img, 'cart_seshion': request.session['my_list']})


def finalOrder(request):
    #товары в корзине
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
        #print(123)
        #print(final)

        cursor = connection.cursor()
        my_price = final[1]
        my_name = final[0]
        my_img = final[2]

        postgreSQL_select_Query_3 = "INSERT INTO shop_orders (tovar_name, price, img) VALUES ('" + my_name + "', '" + my_price + "', '" + my_img + "' )"
        #print(postgreSQL_select_Query_3)
        cursor.execute(postgreSQL_select_Query_3)
        connection.commit()
    request.session['my_list'] = []

    #return render(request, 'shop_app/show.html')
    return render(request, 'shop_app/shop_final.html')


def dell_goods(request):
    #удалить товар(ы) из корзины
    name_dell = request.GET.get('id', default=None)
    print(name_dell)
    i = 0
    session_array = request.session['my_list']
    dell_id = request.session['my_list'][0][1]
    for dell_good in session_array:
        if name_dell == dell_good[0]:
            del session_array[i]
            break
        else:
            i += 1
    request.session['my_list'] = session_array
    print(request.session['my_list'])
    print(321)
    dell_id = str(dell_id)
    print(dell_id)
    connection = psycopg2.connect(user="shopuser",
                                  password="shop_pos0701",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="shop_pos")

    postgreSQL_select_Query = "delete from shop_orders where tovar_name = '" + name_dell + "' and bill_id  = " + dell_id
    print(postgreSQL_select_Query)
    cursor = connection.cursor()
    cursor.execute(postgreSQL_select_Query)
    connection.commit()
    print(request.session['my_list'])

    return render(request, 'shop_app/del_goods.html')

def shop_orders(request):
    session_array = request.session['my_list']
    print('test_array')
    print(session_array)
    button_vis = 'un_visible'
    if len(session_array) > 0:
        button_vis = 'visible'
    return render(request, 'shop_app/shop_orders.html', context={'session_array': session_array, 'bbutton_vis': button_vis})

def send_order(request):
    print('vse_tovari')
    print(request.session['my_list'])
    connection = psycopg2.connect(user="shopuser",
                                  password="shop_pos0701",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="shop_pos")

    search_bill_id = request.session['my_list'][0][3] # в этой строке берем номер нашей корзинки и отправляем в инсерт в таблицу заказов
    print('test_searc')
    print(search_bill_id)
    for finall in request.session['my_list']:
        my_price = finall[1]
        my_name = finall[0]
        my_img = finall[2]
        postgreSQL_select_Query = "INSERT INTO shop_orders (tovar_name, price, img, bill_id) VALUES ('" + my_name + "', '" + my_price + "', '" + my_img + "', " + search_bill_id + " )"
        print(postgreSQL_select_Query)
        cursor = connection.cursor()
        cursor.execute(postgreSQL_select_Query)
        connection.commit()
    request.session['my_list'] = []

    return render(request, 'shop_app/send_order.html')

    #print('test_sess')
    #print(request.session['my_list'])
    #print(show[0][1])

"""    if request.session['my_list'] in locals():
        print('yes')
    else:
        print('no')"""