from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель для пользователя"""

    username = models.CharField(verbose_name='Юзернейм', max_length=50, unique=True)
    email = models.EmailField(verbose_name='Email', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.username} - {self.email}'

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователь'
