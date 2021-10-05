from django.shortcuts import render

from .models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

SITE_TITLE = 'geeks'


def index(request):
    context = {
        'title': SITE_TITLE
    }
    return render(request, 'products/index.html', context)


def products(request, code=None, page_id=1):
    if code is None:
        selected_products = Product.objects.all()
    else:
        selected_products = Product.objects.filter(category_id=code)
    # pagination
    paginator = Paginator(selected_products, per_page=3)
    try:
        pp = paginator.page(page_id)
    except PageNotAnInteger:
        pp = paginator.page(1)
    except EmptyPage:
        pp = paginator.page(paginator.num_pages)

    context = {
        'title': f'{SITE_TITLE}: Каталог',
        'products': pp,
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)
