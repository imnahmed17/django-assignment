from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Product, Review


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


def add_review(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        content = request.POST.get('review_content')
        rating = int(request.POST.get('review_rating'))
        
        Review.objects.create(product=product, content=content, rating=rating)
    
    return redirect('product_details', product_id=product_id)