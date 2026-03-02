from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class MyUserAdmin(UserAdmin):
    """Админка для User"""

    list_display = ('username', 'email', 'is_staff', 'is_active',)
    search_fields = ("username", "email",)
