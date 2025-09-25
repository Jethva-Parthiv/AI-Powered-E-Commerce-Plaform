from products.models import Product

def get_similar_products(product, limit=5):
    """
    Recommend products based on category or tags.
    """
    similar = Product.objects.filter(category=product.category).exclude(id=product.id)[:limit]
    if similar.exists():
        return similar

    # fallback: match by tags
    if product.tags:
        return Product.objects.filter(tags__icontains=product.tags.split(",")[0]).exclude(id=product.id)[:limit]

    return Product.objects.all().exclude(id=product.id)[:limit]
