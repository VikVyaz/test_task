from django.urls import path

from users.apps import UsersConfig

from .views import LogInView, LogOutView, RegisterView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='reg')
]
