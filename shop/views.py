from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category # type: ignore


def shop(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug is not None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        
    else:
        products = Product.objects.all().filter(is_available=True)
    
    product_count = products.count()
    
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'shop.html', context)

# Product detail view for a specific product
def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
    except Exception as e:
        raise e 
    
    context = {
        'single_product': single_product,
    }
    return render(request, 'shop/product_detail.html',context)