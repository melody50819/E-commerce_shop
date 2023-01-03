from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('admin/', admin.site.urls),
    path(
        '',
        RedirectView.as_view(
        pattern_name='products:product_list'),
        name='root'
    ),
]