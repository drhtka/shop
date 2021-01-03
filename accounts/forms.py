# -*- coding: utf-8 -*-

from allauth.account.forms import SignupForm
from django import forms
from .models import *
class SimpleSignupForm(SignupForm):
    phone = forms.CharField(max_length=12, label='Телефон')
    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        user.phone = self.cleaned_data['phone']
        user.save()
        return user