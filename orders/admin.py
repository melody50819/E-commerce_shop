from django.contrib import admin
from orders.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ('user', 'products', 'ordered_at')
    filter_horizontal = ("products",)