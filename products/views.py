from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from orders.models import Order


def product_list(request):
    products = Product.objects.filter(status=Product.Status.UP)
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
def add_to_shopcar(request, id):
    product = get_object_or_404(Product, id=id)
    order, _ = Order.objects.get_or_create(
        user=request.user,
        ordered_at__isnull=True,
    )

    order.products.add(product)
    messages.success(request, '已將產品加入購物車')
    return redirect('products:product_list')