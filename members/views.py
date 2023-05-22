from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from core import models


# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages


# Create your views here.
class TitleMixin:
    title = None

    def get_title(self):
        return self.title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


class LoginUser(TitleMixin, LoginView):
    redirect_authenticated_user = True
    template_name = 'authenticate/login.html'
    context_object_name = 'login'
    title = 'Авторизация'

    def get_success_url(self):
        return reverse_lazy('core:home_page')

    def form_invalid(self, form):
        messages.error(self.request, 'Неверное имя пользователя или пароль')
        return self.render_to_response(self.get_context_data(form=form))



