from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import login
from .forms import RegisterForm


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


class RegisterView(FormView):
    template_name = 'authenticate/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('core:home_page')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)

        return super(RegisterView, self).form_valid(form)
