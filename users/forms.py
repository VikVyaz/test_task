from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .mixins import WhiteMontserratMixin
from .models import User


class AuthForm(WhiteMontserratMixin, AuthenticationForm):
    """Форма для auth"""

    class Meta:
        model = User
        fields = ('email', 'password')


class UserRegisterFrom(WhiteMontserratMixin, UserCreationForm):
    """Форма для регистрации"""

    usable_password = None

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
