# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UsernameField, AuthenticationForm
from django.contrib.auth.models import User

from allauth.account.forms import SignupForm
from django import forms
from .models import *
class SimpleSignupForm(SignupForm):
    #djang-allauth_dop_polya.pdf
    phone = forms.CharField(max_length=12, label='Телефон')
    lead = forms.CharField(max_length=1, label='Лид')
    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        user.phone = self.cleaned_data['phone']
        user.lead = self.cleaned_data['lead']
        user.save()
        return user

class AuthorizationForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'имя'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'пароль макс 12 симолов'}))
    # username = UsernameField(
    #     label=False,
    #     widget=forms.TextInput(attrs={'autofocus': False, 'class': 'form-control', 'placeholder': 'Логин'}), max_length=20)
    # password = forms.CharField(
    #     # label=_("Password"),
    #     label=False,
    #     strip=False,
    #     widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль максимум 12 символов'}),  max_length=12)
    class Meta:
        model = CustomUser
        fields = ("username", "password")

class RegistrationForm(forms.ModelForm):

    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'имя'}), max_length=12)
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'телефон'}), max_length=12)
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'электронная почта'}), max_length=35)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'пароль макс 12 симолов'}), max_length=12)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'пароль еще раз'}), max_length=12)

    class Meta:
        model = CustomUser
        fields = ("password", "phone",  "email", "username", "first_name", )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают")
        return cd["password2"]

class FastRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control input-email', 'placeholder': 'имя'}), max_length=12)
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'телефон'}), max_length=12)
# email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'электронная почта'}), max_length=35)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'пароль макс 12 симолов'}), max_length=12)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'пароль еще раз'}), max_length=12)
    lead = forms.CharField(widget=forms.HiddenInput(), empty_value='1')

    class Meta:
        model = CustomUser
        fields = ("username", "phone", "password", "password2", "lead")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Пароли не совпадают")
        return cd["password2"]

