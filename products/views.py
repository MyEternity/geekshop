import datetime
import json
import os.path

from django.shortcuts import render
from .models import Product, ProductCategory

SITE_TITLE = 'geeks'


def index(request):
    context = {
        'title': SITE_TITLE,
        'current_date': datetime.datetime.now().strftime("%d/%m/%Y")
    }
    return render(request, 'products/index.html', context)


def products(request, code=None):
    if code is None:
        selected_products = Product.objects.all()
    else:
        selected_products = Product.objects.filter(category_id=code)
    context = {
        'title': f'{SITE_TITLE}: Каталог',
        'current_date': datetime.datetime.now().strftime("%d/%m/%Y"),
        'products': selected_products,
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)
