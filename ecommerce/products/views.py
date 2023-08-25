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
        uname = request.POST.get('uname')
        rating = request.POST.get('rating')
        content = request.POST.get('content')
        product = get_object_or_404(Product, pk=product_id)

        if not uname:
            uname = 'Anonymous'

        if rating and content:
            review = Review(review_product=product, review_user=uname, review_rating=rating, review_content=content)
            review.save()
        else:
            messages.error(request, 'Rating and review field required.')
    
    return redirect('products:product_details', product_id=product_id)