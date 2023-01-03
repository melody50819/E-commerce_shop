from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from orders.forms import ShopcarForm
from orders.models import Order


@login_required
def shopcar(request):
    order, _ = Order.objects.get_or_create(
        user=request.user, 
        ordered_at__isnull=True,
    )
    form = ShopcarForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        messages.success(request, '編輯成功')
        return redirect('orders:shopcar')

    return render(request, 'orders/shopcar.html', {'form': form})


@login_required
def shopcar_submit(request):
    if request.method != 'POST':
        messages.warning(request, '請重新點選下單')
        return redirect('orders:shopcar')

    order, _ = Order.objects.get_or_create(
        user=request.user, 
        ordered_at__isnull=True,
    )

    if order.products.count() < 1:
        messages.warning(request, '此購物車無產品')
        return redirect('products:product_list')

    order.ordered_at = timezone.now()
    order.save()
    messages.success(request, '下單成功')
    return redirect('products:product_list')

@login_required
def order_list(request):
    orders = Order.objects.filter(
        user=request.user, 
        ordered_at__isnull=False,
    )

    return render(request, 'orders/order_list.html', {'orders': orders})