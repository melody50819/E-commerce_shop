from django.urls import path

from orders.views import shopcar, shopcar_submit, order_list


app_name = 'orders'

urlpatterns = [
    path('shopcar/', shopcar, name='shopcar'),
    path('shopcar/submit/', shopcar_submit, name='shopcar_submit'),
    path('', order_list, name='order_list'),
]