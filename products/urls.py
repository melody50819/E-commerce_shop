from django.urls import path

from products.views import product_list, product_detail, add_to_shopcar

app_name = 'products'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:id>/', product_detail, name='product_detail'),
    path('<int:id>/add-to-shopcar', add_to_shopcar, name='add_to_shopcar'),
]