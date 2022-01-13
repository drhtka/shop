import random

from allauth.account.views import logout
from django.contrib import auth
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic, View
from accounts.forms import RegistrationForm, FastRegistrationForm, AuthorizationForm
from django.http import HttpResponseRedirect, HttpResponse
from accounts.models import CustomUser
from shop_app.models import BillingModel, OrdersModel, Image


def accounts(request):
    return render(request, 'accounts.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            # return render(request, "accounts/sign_up_bac.html",
            #               {"new_user": new_user})
            # if not request.user.is_authenticated():/
            return HttpResponseRedirect('/login/')
    else:
        form = RegistrationForm()

    return render(request, "accounts/register.html", {"user_form": form})


# class SignUpView(View):
#      # form_class = AuthenticationForm
#      # success_url = reverse_lazy('.')
#      # template_name = 'shop_app/big_retail/fast_check-out.html'
#      def post(self, request, *args, **kwargs):
#           form_aut = AuthorizationForm(request.POST)
#           form = FastRegistrationForm()
#           if form_aut.is_valid():
#                cd = form_aut.cleaned_data
#                user = authenticate(
#                     request,
#                     username=cd['username'],
#                     password=cd['password']
#                )
#                if user is None:
#                     return HttpResponse('Неправильный логин и/или пароль')
#                if not user.is_active:
#                     return HttpResponse('Ваш аккаунт заблокирован')
#
#                login(request, user)
#                return HttpResponse('Добро пожаловать! Успешный вход')
#
#           return render(request, 'shop_app/big_retail/fast_check-out.html', {'form_aut': form_aut,
#                                                                         'user_formm': form,})
#
#      def get(self, request, *args, **kwargs):
#           form = FastRegistrationForm()
#           form_aut = AuthorizationForm()
#           return render(request, 'shop_app/big_retail/fast_check-out.html', {'form_aut': form_aut,
#                                                                         'user_formm': form,})
# User = get_user_model()
# def login_view(request):
#      form = FastRegistrationForm()
#      form_aut= AuthorizationForm(request.POST or None)
#      if form.is_valid():
#           data = form.cleaned_data
#           username = data.get('username')
#           password = data.get('password')
#           user = authenticate(request, username=username, password=password)
#           login(request, user)
#           return redirect('home')
#      return render(request, 'shop_app/big_retail/fast_check-out.html', {'form_aut': form_aut,
#                                                                    'user_formm': form,})

def user_login(request):
    # sign_up
    if request.method == 'POST':
        form_aut = AuthorizationForm(data=request.POST)
        form_fast = FastRegistrationForm()
        if form_aut.is_valid():
            user = form_aut.get_user()
            login(request, user)
            return HttpResponseRedirect('/shop_orders/')
            # return render(request, 'shop_app/big_retail/fast_check-out.html', {'form_aut': form_aut,
            #                                                               'user_formm': form_fast,})
    else:

        form_aut = AuthorizationForm()
        form_fast = FastRegistrationForm()
    # return render(request, 'signup.html', {"form_aut": form_aut,
    #                                         'user_formm': form_fast})
    return render(request, 'shop_app/big_retail/check-out.html', {'form_aut': form_aut,
                                                                  'user_formm': form_fast, })


# @login_required(login_url=reverse_lazy('login'))
def authorization(request):
    #  страница финальная, где подтверждаются все заказы старый shop_orders.html'
    # sum_append = []
    form = AuthorizationForm()
    # print("ses-1")
    # print(request.session.get('my_list'))
    print('author-shop')
    print(request.user)
    if request.method == 'GET':
        return render(request, 'authorization/authorization.html', context={'form': form, })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'authorization/authorization.html',
                          {'form': AuthenticationForm(), 'error': 'Пароль или пользователь не верный'})
        else:
            login(request, user)
            return redirect('/')



"""                                                                           
    else:
        empty_cart = 'Корзина пуста!'
        form_aut = AuthorizationForm()
        form = FastRegistrationForm()
        button_vis = 'un_visible'
        # request.session['my_list'] = []
        # button_vis = 'un_visible'
        # if len(request.session.get('my_list')) > 0:
        #     print('сессия есть--')
        # else:
        #     print('сессия net')
        return render(request, 'shop_app/big_retail/check-out.html', {'empty_cart': empty_cart,
                                                                      'user_formm': form,
                                                                      'form_aut': form_aut,
                                                                      'button_vis': button_vis,
                                                                      'username': auth.get_user(request).username, })

"""


def user_logout(request):
    logout(request)
    return redirect('/')


# @login_required(login_url=reverse_lazy('login'))
def fastregister(request):
    # test_form = FastRegistrationForm()
    # print('test_form')
    # # print(test_form)
    # # button_vis = 'visible'
    #
    # print("ses-1")
    # print(request.session.get('my_list'))
    # print('author-shop')
    # print(request.user)
    # summ = 0
    # name = ''
    # new_user = ''
    # if request.session.get('my_list'):
    #
    #     print('сессия есть')
    #     button_vis = 'visible'
    #     session_array = request.session['my_list']
    #     render_session = request.session['my_list']
    #     count_render_session = len(session_array)
    #     summ = 0
    #     name = ''
    #     for session_array_s in session_array:
    #         summ += int(session_array_s[1])
    #         name = session_array_s[0]
    #     insert_order = BillingModel(sum=summ,
    #                                 user_cart=request.user.username, )  # заносим в базу
    #     insert_order.save(force_insert=True)  # сохраняем в базу
    #     for insert_order_s in session_array:
    #         nearly_final = OrdersModel(bill_id=insert_order.id,
    #                                    tovar_name=insert_order_s[0],
    #                                    price=insert_order_s[1],
    #                                    img=insert_order_s[2], )
    #         nearly_final.save(force_insert=True)
    #     nearly_final_text = ' Авторизируйтесь для окначания покупки'
    #     # request.session['my_list'] = []
    #     # button_vis = 'un_visible'
    #     # if len(request.session.get('my_list')) > 0:
    #     #     button_vis = 'visible'
    #     #     print('сессия есть--')
    #     # else:
    #     #     print('сессия net')
    #     gallery_index = Image.objects.filter(object_id=16).values_list()
    #     gallery_index_tmp = random.sample(list(gallery_index), 16)

    if request.method == "POST":
        # print('method PoST')
        form = FastRegistrationForm(request.POST)
        # form_aut = AuthorizationForm()
        # print('form-1-1')
        # print(form)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            # print('new_user')
            # print(new_user)
            # button_viss = 'un_visible'
            # return render(request, "fast_check-out-bac.html",
            #                                   {'session_array': session_array,
            #                                    'button_viss': button_viss,
            #                                    'button_vis': button_vis,
            #                                    "form_aut": form_aut,
            #                                    'count_render_session': count_render_session,
            #                                    'render_session': render_session,
            #                                    'summ': summ,
            #                                    'gallery_index_tmp': gallery_index_tmp,
            #                                    'main_summ_cart': request.session['summ'],
            #                                    'user_formm': form,
            #                                    'nearly_final_text': nearly_final_text,
            #                                    'new_user': new_user
            #                                    })
            # if not request.user.is_authenticated():
            return HttpResponseRedirect('/login/')
    else:
        # empty_cart = 'Корзина пуста!'
        # form = FastRegistrationForm()
        # form_aut = AuthorizationForm()
        # button_viss = 'visible'
        # button_vis = 'un_visible'
        # print('method get')
        # return render(request, "fast_check-out-bac.html", {'empty_cart': empty_cart,
        #                                                    "user_formm": form,
        #                                                    "form_aut": form_aut,
        #                                                    'button_viss ': button_viss,
        #                                                    'button_vis': button_vis,
        #                                                    'new_user': new_user, })

        if request.method == "POST":
            form = FastRegistrationForm(request.POST)
            # form_aut = AuthorizationForm()
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.set_password(form.cleaned_data["password"])
                new_user.save()
                print('new_user')
                print(new_user)
                # button_viss = 'un_visible'
                # return render(request, "fast_check-out-bac.html",
                #                                   {'session_array': session_array,
                #                                    'button_viss': button_viss,
                #                                    'button_vis': button_vis,
                #                                    "form_aut": form_aut,
                #                                    'count_render_session': count_render_session,
                #                                    'render_session': render_session,
                #                                    'summ': summ,
                #                                    'gallery_index_tmp': gallery_index_tmp,
                #                                    'main_summ_cart': request.session['summ'],
                #                                    'user_formm': form,
                #                                    'nearly_final_text': nearly_final_text,
                #                                    'new_user': new_user
                #                                    })
                # if not request.user.is_authenticated():
                return HttpResponseRedirect('/login/')

        # return HttpResponseRedirect('/login/')
# def form_valid(self, form):
#      form.instance.password=self.password
#      return super().form_valid(form)

# def form_valid(self, form):
#      # print 'happening2'
#      # form.instance.save()
#      # self.user.teams.add(form.instance)
#      form.save()
# return super(form_valid, self).form_valid(form)

# def form_valid(self, commit=True):
#      user = super().save(commit=False)
#      user.set_password(self.cleaned_data["password1"])
#      if commit:
#           user.save()
#      return user

# def form_valid(self, form):
#      print('form')
#      print(form)
#      print("pass")
#      print(form.cleaned_data["password"])
#      # print('Form')
#      # print(Fform.email)
#      b2 = CustomUser(email=form.cleaned_data["email"])
#      b2.save()
#      print('b2.id')
#      print(b2.id)
# new_user = form.save(commit=False)
# new_user.set_password(form.cleaned_data["password"])
# print('new')
# print(new_user)
# new_user.save()


# self.new_user = form.save(commit=False)
# self.new_user.set_password(form.cleaned_data["password"])
# self.new_user.password = self.new_user.password
# self.new_user.email = self.new_user.email
# print('new')
# print(self.new_user)
# self.new_user.save()
# return super().form_valid(form)
