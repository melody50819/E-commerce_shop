from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(
        to=User, 
        on_delete=models.PROTECT, 
        related_name='orders',
    )

    products = models.ManyToManyField(to=Product, related_name='orders')
    ordered_at = models.DateTimeField(null=True, blank=True)  # 下單日期 有下單日期＝有下單

