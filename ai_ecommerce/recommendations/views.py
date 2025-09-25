from django.shortcuts import render, get_object_or_404
from products.models import Product
from .engine import get_similar_products

def recommended_products(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    recommendations = get_similar_products(product)
    return render(request, 'recommendations/recommended_products.html', {
        'product': product,
        'recommendations': recommendations
    })
