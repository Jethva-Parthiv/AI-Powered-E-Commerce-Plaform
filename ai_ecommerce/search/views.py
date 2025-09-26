from django.shortcuts import render
from .engine import search_products

def search_view(request):
    query = request.GET.get('q', '')
    results = search_products(query) if query else []
    print("DEBUG >>> query:", query, "results:", results)  # for debugging
    return render(request, 'search/search_results.html', {
        'query': query,
        'results': results
    })
