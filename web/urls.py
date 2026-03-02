from django.urls import path

from web.apps import WebConfig
from web.views import MainPageView

app_name = WebConfig.name

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
]
