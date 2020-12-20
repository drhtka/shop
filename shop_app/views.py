# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
import psycopg2
from django.http import HttpResponse
from django.template import loader, Context
from django.urls import reverse

from shop_app.models import GoodsModel, Image, CategoryModel, Product
import random

def index(request):
    #главная
    # print('index_sess-1')
    # print(request.session.get('my_list'))
    all_goods_arr = []
    all_goods = GoodsModel.objects.values_list()
    all_goods_random = all_goods
    all_goods_arr.append(all_goods)
    all_goods = all_goods_arr
#start
    # all_goods_random = random.sample(list(all_goods_random), 7)
    # print('all_goods_random')
    # print(all_goods_random)
#end
    tmp_append_goods = []
    tmp_categ_name = []
    tmp_categ_name_list = []
    for all_goods_s in all_goods:
        tmp_append_goods.append(all_goods_s)
        for tmp_s in tmp_append_goods[0]:
            #print('tmp_s')
            #print(tmp_s)
            p = GoodsModel(category=tmp_s[2])
            categor_name = p.get_category_display()
            list_tmp = list(tmp_s)
            list_tmp[2]=categor_name
            list_tmp = tuple(list_tmp)
            for list_tmp_s in [list_tmp]:
                tmp_categ_name_list = list_tmp_s
                tmp_categ_name.append(tmp_categ_name_list)
        all_goods_random = random.sample(list(tmp_categ_name), 7)

        render_session = []
        if request.session.get('my_list'):
            # print('index_sess-2')
            # print(request.session['my_list'])
            render_session = request.session['my_list']
        count_render_session = len(render_session)
        gallery_index_tmp = []
        gallery_index = Image.objects.filter(object_id=16).values_list()
        gallery_index_tmp = random.sample(list(gallery_index), 16)
        # print('gallery_index_tmp')
        # print(gallery_index_tmp)

        return render(request, 'shop_app/index.html', {'all_goods': tmp_categ_name,
                                                       'all_in_slider': all_goods[0:5],
                                                       'render_session': render_session,
                                                       'count_render_session': count_render_session,
                                                       'all_goods_random': all_goods_random,
                                                       'gallery_index_tmp': gallery_index_tmp,
                                                       })

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

    return render(request, 'shop_app/contacts.html', context={'contacts': 'hello', 'mobile_records': mobile_records})

def goods(request):
    # все товары по определённой категории
    # print('1234')
    #idcat = request.GET.get('i', default=None)
    all_goods_arr = []
    connection = psycopg2.connect(user="shopuser",
                                  password="shop_pos0701",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="shop_pos")
    cursor = connection.cursor()
    postgreSQL_select_Query = 'select * from goods'
    cursor.execute(postgreSQL_select_Query)
    goodss = cursor.fetchall()

    postgreSQL_select_Query = "select * from goods ORDER BY id ASC"
    # print(postgreSQL_select_Query)
    cursor.execute(postgreSQL_select_Query)
    goodss = cursor.fetchall()
    # print('goodss')
    # print(goodss)
    all_goods_arr.append(goodss)
    all_goods = all_goods_arr


    tmp_append_goods = []
    tmp_categ_name = []
    tmp_categ_name_list = []
    for all_goods_s in all_goods:
        tmp_append_goods.append(all_goods_s)
        for tmp_s in tmp_append_goods[0]:
            #print('tmp_s')
            #print(tmp_s)
            p = GoodsModel(category=tmp_s[2])
            categor_name = p.get_category_display()
            list_tmp = list(tmp_s)
            list_tmp[2]=categor_name
            list_tmp = tuple(list_tmp)
            #print('tmPP_turp')
            #print(list_tmp)
            for list_tmp_s in [list_tmp]:
                # print('list_tmp_s')
                # print(list_tmp_s)
                tmp_categ_name_list = list_tmp_s
                tmp_categ_name.append(tmp_categ_name_list)
    # print('tmp_categ_name')
    # print(tmp_categ_name)
    category_on_goods = CategoryModel.objects.values_list()


    return render(request, 'shop_app/big_retail/shop-list.html', context={'goods': tmp_categ_name,
                                                                          'category_on_goods': category_on_goods})
def sort_goods_categ(request):
    # сортировка по категориям
    # print('ii')
    # print(request.GET.get('i'))
    cat_num = (request.GET.get('i'))
    sort_goods_categ = GoodsModel.objects.filter(category=str(cat_num)).values_list()
    tmp_append_goods = []
    tmp_categ_name = []
    tmp_categ_name_list = []
    for all_goods_s in sort_goods_categ:
        tmp_append_goods.append(all_goods_s)
    # print('tmp_append_goods')
    # print(tmp_append_goods)
        # print('all_goods_s')
        # print(all_goods_s)


    for tmp_s in tmp_append_goods:
        # print('tmp_s')
        # print(tmp_s[2])
        p = GoodsModel(category=tmp_append_goods[0][2])
        categor_name = p.get_category_display()
        list_tmp = list(tmp_s)
        list_tmp[2]=categor_name
        list_tmp = tuple(list_tmp)
        # print('list_tmp')
        # print(list_tmp)
        for list_tmp_s in [list_tmp]:
            tmp_categ_name_list = list_tmp_s
            tmp_categ_name.append(tmp_categ_name_list)

    category_on_goods = CategoryModel.objects.values_list()
    return render(request, 'shop_app/big_retail/shop-list.html', context={'goods': tmp_categ_name,
                                                                          'category_on_goods': category_on_goods})

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
    # отправка на страницу в корзину и количество товаров header-top
    render_session = []
    if request.session.get('my_list'):
        render_session = request.session['my_list']
    count_render_session = len(render_session)
    return render(request, 'shop_app/big_retail/portfolio.html', context={'category': category, 'render_session': render_session, 'count_render_session': count_render_session})

def gallery(request):
    all_photo = Image.objects.values_list()
    for all_photo_s in all_photo:
        print(all_photo_s[1])
    #return render(request, 'shop_app/category.html')
    return render(request, 'shop_app/big_retail/portfolio.html', {'all_photo': all_photo_s})
#from django.contrib.admin.options import get_content_type_for_model
def show(request, pk):
    # детальное описание товара
    print('id')
    print(pk)
    #idgoods = request.GET.get('i', default=None)
    connection = psycopg2.connect(user="shopuser",
                                  password="shop_pos0701",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="shop_pos")

    if pk:
        idgoods = str(pk)
        postgreSQL_select_Query = "select * from goods where id = " + idgoods + " ORDER BY id ASC"
    else:
        postgreSQL_select_Query = "select * from goods ORDER BY id ASC"
    cursor = connection.cursor()
    cursor.execute(postgreSQL_select_Query)
    show = cursor.fetchall()
    test_ashow = show[0][1]
    chek_good = ''
    if request.session.get('my_list'):
        show_get = request.session['my_list']
        for ts in show_get:
            if ts[0] == test_ashow:
                chek_good = 'disabled'
                break

    # print(request.session['my_list'])
    #symbol = GoodsModel.objects.first()
    #image_goods = Image.objects.filter(content_type=get_content_type_for_model(symbol), object_id=request.GET.get('i'))
    image_goods = Image.objects.filter(object_id=pk).values_list()

    # all_goods = GoodsModel.objects.values_list()
    # # print('all_goods_show')
    # # print(all_goods)
    # all_goods_random = random.sample(list(all_goods), 7)
    all_goods_arr = []
    all_goods = GoodsModel.objects.values_list()
    all_goods_random = all_goods
    all_goods_arr.append(all_goods)
    all_goods = all_goods_arr
    #start
    # all_goods_random = random.sample(list(all_goods_random), 7)
    # print('all_goods_random')
    # print(all_goods_random)
    #end
    tmp_append_goods = []
    tmp_categ_name = []
    tmp_categ_name_list = []
    for all_goods_s in all_goods:
        tmp_append_goods.append(all_goods_s)
        for tmp_s in tmp_append_goods[0]:
            #print('tmp_s')
            #print(tmp_s)
            p = GoodsModel(category=tmp_s[2])
            categor_name = p.get_category_display()
            list_tmp = list(tmp_s)
            list_tmp[2]=categor_name
            list_tmp = tuple(list_tmp)
            for list_tmp_s in [list_tmp]:
                tmp_categ_name_list = list_tmp_s
                tmp_categ_name.append(tmp_categ_name_list)
        all_goods_random = random.sample(list(tmp_categ_name), 7)
    tegs_categ = CategoryModel.objects.filter(id=show[0][2]).values('description')

    tegs_categ_desc = tegs_categ[0]['description']
    # отправка на страницу в корзину и количество товаров header-top
    render_session = []
    if request.session.get('my_list'):
        render_session = request.session['my_list']
    count_render_session = len(render_session)
    # отправка на страницу в корзину и количество товаров header-top
    #'render_session': render_session, 'count_render_session': count_render_session
    tmp_append_goods = []
    tmp_categ_name = []
    tmp_categ_name_list = []
    for all_goods_s in show:
        tmp_append_goods.append(all_goods_s)
        # print('tmp_append_goods')
        # print(tmp_append_goods)
        for tmp_s in tmp_append_goods:
            # print('tmp_s')
            # print(tmp_s)
            p = GoodsModel(category=tmp_s[2])
            categor_name = p.get_category_display()
            list_tmp = list(tmp_s)
            list_tmp[2]=categor_name
            list_tmp = tuple(list_tmp)
            #print('tmPP_turp')
            #print(list_tmp)
            for list_tmp_s in [list_tmp]:
                print('list_tmp_s')
                print(list_tmp_s)

        return render(request, 'shop_app/big_retail/shop-detail.html', context={'show': list_tmp_s,
                                                                                'chek_good': chek_good,
                                                                                'image_goods': image_goods, 'tegs_categ_desc': tegs_categ_desc,
                                                                                'all_goods_random': all_goods_random,
                                                                                'render_session': render_session,
                                                                                'count_render_session': count_render_session,

                                                                                })
    #return render(request, 'shop_app/showp.html', context={'show': show, 'chek_good': chek_good})

def shop_billing(request):
    request.session.modified = True
    #выбираем товар и отправляем в корзину
    #id_shop_billing = request.POST.get('i', default=None)
    # request.session['my_list'] = []
    connection = psycopg2.connect(user="shopuser",
                                  password="shop_pos0701",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="shop_pos")

    id_shop_billing = request.GET.get('i')
    name = request.GET.get('name')
    price = request.GET.get('price')
    img = request.GET.get('img')
    #img = str(img)
    print(type(img))

    if len(request.session['my_list']) > 0:
        print(request.session['my_list'])
        search_find_id = request.session['my_list'][0][3]
        request.session['my_list'].append([name, price, img, search_find_id])
    else:
        # request.session['my_list'] = []
        postgreSQL_select_Query = "INSERT INTO shop_billing (name, sum) VALUES ('" + name + "', '" + price + "')"
        #вставляем запись в таблицу shop_billing - эта запись будет номером корзинки 26 min
        # print(postgreSQL_select_Query)
        cursor = connection.cursor()
        cursor.execute(postgreSQL_select_Query)
        connection.commit()

        postgreSQL_select_Query = "SELECT * FROM shop_billing ORDER BY id DESC LIMIT 1"
        # после вставки получаем номер этой записи (номер корзинки)
        cursor = connection.cursor()
        cursor.execute(postgreSQL_select_Query)
        show = cursor.fetchone()
        # print(show[0])
        find_id = str(show[0])
        # print('type(find_id)')
        # print(find_id)
        # print(type(find_id))

        request.session['my_list'].append([name, price, img, find_id])


    # print(request.session['my_list'])
    return render(request, 'shop_app/shop_billing.html', context={'name': name, 'price': price, 'img': img, 'cart_seshion': request.session['my_list']})

def shop_cart(request):
    #выбираем товар и отправляем в корзину
    # print('shop_cart-1')
    # print(request.session.get('my_list'))
    request.session.modified = True
    connection = psycopg2.connect(user="shopuser",
                                  password="shop_pos0701",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="shop_pos")

    id_shop_billing = request.GET.get('i')
    name = request.GET.get('name')
    price = request.GET.get('price')
    img = request.GET.get('img')
    # img = str(img)
    # print(type(img))
    name = str(name)
    price = str(price)
    request.session.get('my_list')
    if request.session.get('my_list'):
        request.session['summ'] = int(price) + int(request.session['summ'])
        search_find_id = request.session['my_list'][0][3]
        # print('search_find_id')
        # print(search_find_id)
        request.session['my_list'].append([name, price, img, search_find_id, 1, id_shop_billing, price])


    else: # сразу идет сюда и заносит парвым в корзину
        # request.session['my_list'] = []
        request.session['summ'] = price
        my_list_cart = []
        postgreSQL_select_Query = "INSERT INTO shop_billing (name, sum) VALUES ('" + name + "', '" + price + "')"
        #вставляем запись в таблицу shop_billing - эта запись будет номером корзинки 26 min
        cursor = connection.cursor()
        cursor.execute(postgreSQL_select_Query)
        connection.commit()

        postgreSQL_select_Query = "SELECT * FROM shop_billing ORDER BY id DESC LIMIT 1"
        # после вставки получаем номер этой записи (номер корзинки)
        cursor = connection.cursor()
        cursor.execute(postgreSQL_select_Query)
        show = cursor.fetchone()
        find_id = str(show[0])
        # print('find_id')
        # print(find_id)
        my_list_cart.append([name, price, img, find_id, 1, id_shop_billing, price]) # сразу идет сюда добавил 1 для счетчика
        request.session['my_list'] = my_list_cart
    print('уход на рефферер')
    print(request.session['my_list'])
    # referer = self.request.META.get('HTTP_REFERER')# вернуться на предыдущую страницу на тот же урл
    return redirect(request.META.get('HTTP_REFERER'))
    # return redirect('/')
    # return render(request, 'shop_app/big_retail/cart.html', context={'name': name, 'price': price, 'img': img, 'cart_seshion': request.session['my_list']})

def shop_bay(request):
    # товары в корзине прорисовываем в шаблоне
    all_goods_arr = []
    all_goods = GoodsModel.objects.values_list()
    all_goods_arr.append(all_goods)
    all_goods = all_goods_arr
    tmp_append_goods = []
    tmp_categ_name = []
    tmp_categ_name_list = []
    for all_goods_s in all_goods:
        tmp_append_goods.append(all_goods_s)
        for tmp_s in tmp_append_goods[0]:
            #print('tmp_s')
            #print(tmp_s)
            p = GoodsModel(category=tmp_s[2])
            categor_name = p.get_category_display()
            list_tmp = list(tmp_s)
            list_tmp[2]=categor_name
            list_tmp = tuple(list_tmp)
            for list_tmp_s in [list_tmp]:
                tmp_categ_name_list = list_tmp_s
                tmp_categ_name.append(tmp_categ_name_list)
        # all_goods_random = random.sample(list(tmp_categ_name), 7)

    all_goods_random = random.sample(list(tmp_categ_name), 9)
    # print('all_goods_random_temp')
    # print(all_goods_random)
    #'all_goods_random': all_goods_random,
    request.session.modified = True
    # print('shop_bay-1')
    # print(request.session.get('my_list'))
    render_session = []
    cart_seshion = []
    if request.session.get('my_list'):
        cart_seshion = request.session['my_list']
        # print('shop_bay_cart_seshion')
        # print(len(cart_seshion))
        # print('shop_bay-2')
        # print(request.session.get('my_list'))
        # count_cart_session = len(cart_seshion)
        if request.session.get('my_list'):
            render_session = request.session['my_list']
            count_render_session = len(cart_seshion)

        return render(request, 'shop_app/big_retail/cart.html', context={'cart_seshion': cart_seshion,
                                                                         'count_render_session': count_render_session,
                                                                         'render_session': render_session,
                                                                         'all_goods_random': all_goods_random,
                                                                         'main_summ_cart': request.session['summ'],
                                                                         })
    else:
        # return HttpResponse('товаров нэма!')
        all_goods = GoodsModel.objects.values_list()
        all_goods_random = random.sample(list(all_goods), 9)
        print('all_goods_random_temp')
        print(all_goods_random)
        nema = 'Корзина пуста!'
        return render(request, 'shop_app/big_retail/cart.html', context={'nema': nema,
                                                                         'all_goods_random': all_goods_random,})


def finalOrder(request):
    # функция плюсования и минусования
    if request.session.get('my_list'):
        name = request.GET.get('name')
        count = request.GET.get('count')
        prodid = request.GET.get('prodid')
        for sessin_plus in request.session['my_list']:
            if sessin_plus[0] == name:
                sessin_plus[4] += 1 #количество нажатий на плюс
                summ_plus = int(sessin_plus[1]) * int(sessin_plus[4]) #умножаем на количество
                sessin_plus[6] = summ_plus  # записываем в  сессию общую умноженную сумму
                request.session['summ'] = int(request.session['summ']) + int(sessin_plus[1])

                return HttpResponse(sessin_plus[6])
                break
            if sessin_plus[5] == prodid:
                sessin_plus[4] -= 1 #количество нажатий на минус
                print('summ_plus1')
                print(sessin_plus[6])
                summ_plus = int(sessin_plus[6]) - int(sessin_plus[1]) #вычитаем сумму товара из общ суммы
                print('summ_plus2')
                print(summ_plus)
                sessin_plus[6] = summ_plus  # записываем в  сессию общую умноженную сумму
                request.session['summ'] = int(request.session['summ']) - int(sessin_plus[1]) # записываем в  сессию общей суммы всех товаров
                                                                                            # разницу между общей суммой и одного стоимости одного товра при нажатии
                return HttpResponse(sessin_plus[6])
                break
        # return render(request, 'shop_app/big_retail/cart.html', context={'main_summ_cart': request.session['summ'],})
        #                                                                  })
            # return render(request, 'shop_app/big_retail/cart.html', context={'main_summ_cart': request.session['summ'],
            #                                                                  })
            # if sessin_plus[0] == name or sessin_plus[5] == prodid:

        # print('afret_for')
        # print(len(request.session['my_list']))
        # return HttpResponse('Okey')


def dell_goods(request):
    #удалить товар(ы) из корзины
    name_dell = request.GET.get('id') # хоть и напиано id мы ловим name
    print('name_dell')
    print(name_dell)
    name_dell = str(name_dell)
    i = 0
    i = int(i)
    if request.session.get('my_list'):
        session_array = request.session['my_list']
        dell_id = request.session['my_list'][0][1]
        # request.session['summ']
        for dell_good in session_array:

            if name_dell == dell_good[0]: # если имя совпадает тогда удаляем по номеру заданному [i]
                request.session['summ'] = int(request.session['summ']) - int(session_array[i][6]) # записываем в сессию общей суммы разницу общей суммы и суммы всего товара в корзине
                print('session_array')
                print(session_array)
                print(session_array[i])
                del session_array[i] # если имя совпадает тогда удаляем по номеру заданному [i]
                break
            i += 1
        request.session['my_list'] = session_array
    #     return redirect('/category/')
    else:
        return redirect(reverse('index'))
    return redirect(request.META.get('HTTP_REFERER'))

def shop_orders(request):
    #  страница финальная, где подтверждаются все заказы старый shop_orders.html'
    # sum_append = []
    if request.session.get('my_list'):
        session_array = request.session['my_list']
        render_session = request.session['my_list']
        count_render_session = len(session_array)
        print('test_array')
        print(session_array)
        summ = 0
        for session_array_s in session_array:

            summ += int(session_array_s[1])
        print('summ')
        print(summ)
        button_vis = 'un_visible'
        if len(session_array) > 0:
            button_vis = 'visible'
        # sum_prod = sum(session_array[0][1])
        gallery_index = Image.objects.filter(object_id=16).values_list()
        gallery_index_tmp = random.sample(list(gallery_index), 16)


    #'count_render_session': count_render_session, 'render_session': render_session
        return render(request, 'shop_app/big_retail/check-out.html', context={'session_array': session_array,
                                                                              'bbutton_vis': button_vis,
                                                                               'count_render_session': count_render_session,
                                                                               'render_session': render_session,
                                                                               'summ': summ,
                                                                               'gallery_index_tmp': gallery_index_tmp},)
    else:
        empty = 'Корзина пуста!'
        return render(request, 'shop_app/big_retail/check-out.html', {'empty': empty})
def send_order(request):
    # конец всех заказов, очищаем сессию заносим в базу заказ
    print('send_order-1')
    print(request.session.get('my_list'))
    if request.session.get('my_list'):
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
        # print('send_order-2')
        # print(request.session.get('my_list'))
        gallery_index = Image.objects.filter(object_id=16).values_list()
        gallery_index_tmp = random.sample(list(gallery_index), 16)
        return render(request, 'shop_app/send_order.html', {'gallery_index_tmp': gallery_index_tmp})

    #print('test_sess')
    #print(request.session['my_list'])
    #print(show[0][1])

"""    if request.session['my_list'] in locals():
        print('yes')
    else:
        print('no')"""