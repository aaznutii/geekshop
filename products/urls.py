
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from products.views import products, ProductDetail

app_name = "products"

urlpatterns = [
    path('', products, name='products'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('page/<int:page>', products, name='page'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
