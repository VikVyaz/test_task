from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import AuthForm, UserRegisterFrom


class LogInView(LoginView):
    """Логин view для User"""

    template_name = 'users_app/login.html'
    authentication_form = AuthForm
    next_page = ''


class LogOutView(LogoutView):
    """Логаут для User"""

    next_page = ''


class RegisterView(CreateView):
    """View для регистрации"""

    template_name = 'users_app/reg.html'
    form_class = UserRegisterFrom
    success_url = reverse_lazy('web:main_page')
