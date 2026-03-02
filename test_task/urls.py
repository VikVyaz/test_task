from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from test_task import settings

urlpatterns = [
    path('', include('web.urls', namespace='web')),
    path('admin/', admin.site.urls),
    path('user/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
