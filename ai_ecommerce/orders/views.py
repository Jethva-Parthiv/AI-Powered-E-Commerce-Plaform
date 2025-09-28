from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order, OrderItem
from decimal import Decimal

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user).select_related('product')
    cart_total = sum((item.subtotal for item in cart_items), Decimal("0.00"))

    if request.method == "POST":
        payment_method = request.POST.get("payment_method", "cod")

        order = Order.objects.create(
            user=request.user,
            payment_method=payment_method,
            status="pending" if payment_method != "cod" else "paid"
        )

        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        if payment_method == "cod":
            cart_items.delete()
            return render(request, "orders/checkout_success.html", {"order": order})

        elif payment_method == "mock":
            # Simulate online payment success
            order.status = "paid"
            order.save()
            cart_items.delete()
            return render(request, "orders/checkout_success.html", {"order": order})

    return render(request, "orders/checkout.html", {"cart_items": cart_items, "cart_total": cart_total})



@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    # orders_item = OrderItem.objects.filter(order__in=orders).select_related('product', 'order')
    return render(request, "orders/history.html", {"orders": orders})
