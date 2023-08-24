from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Product


def product_list(request):
    query = request.GET.get('search_field', '')
    products = Product.objects.all().order_by('products_id')
    
    if 'search_field' in request.GET:
        if not query:
            messages.error(request, 'Please enter a search query.')
        elif len(query) < 3:
            messages.error(request, 'Please enter at least 3 characters.')
        else:
            products = products.filter(products_name__icontains=query) 

    return render(request, 'products/product_list.html', {'products': products, 'query': query})


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/product_details.html', {'product': product})