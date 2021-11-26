
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from auth_app.views import login, register, logout

app_name = "auth_app"

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
