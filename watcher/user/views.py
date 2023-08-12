# from django.shortcuts import render
# from django.http import HttpResponse
# from django.views import View
# from django.http import HttpResponse
from typing import Any, Dict, Optional
from django.db import models
from django.http import HttpResponse
from django.contrib.auth import login, get_user_model
from django.views.generic import FormView, UpdateView, DetailView
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache

User = get_user_model()

class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'user/register.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
#############################################
class LoginView(FormView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = '/'

    def form_valid(self, form):
        login(self.request, form.cleaned_data['user'])
        return super().form_valid(form)
    # def form_valid(self, form):
    #     user = authenticate() #if user is exist everything is fine!
#############################################
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ('username', 'avatar', 'bio', 'website')
    template_name = 'user/profile_update.html'
    success_url = '/'

    def get_object(self, queryset=None) :
        return self.request.user
#############################################
