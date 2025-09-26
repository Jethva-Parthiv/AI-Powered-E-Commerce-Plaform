from products.models import Product

def search_products(query):
    """
    Simple keyword search across product name, description, and tags.
    """
    results = Product.objects.filter(
        name__icontains=query
    ) | Product.objects.filter(
        description__icontains=query
    ) | Product.objects.filter(
        tags__icontains=query
    )
    return results.distinct()
