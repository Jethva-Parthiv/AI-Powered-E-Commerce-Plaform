from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from cart.models import CartItem
from .models import Order, OrderItem

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_total = sum(item.subtotal for item in cart_items)
    if not cart_items.exists():
        return render(request, "orders/checkout.html", {"error": "Your cart is empty."})

    if request.method == "POST":
        # Create a new order
        order = Order.objects.create(user=request.user, status="pending")

        # Move cart items into order items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price,
            )

        # Clear the cart
        cart_items.delete()

        return render(request, "orders/checkout_success.html", {"order": order})

    return render(request, "orders/checkout.html", {"cart_items": cart_items, "cart_total": cart_total})


