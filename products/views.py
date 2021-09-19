import datetime
import json
import os.path

from django.shortcuts import render
from .models import Product

SITE_TITLE = 'geeks'


def index(request):
    context = {
        'title': SITE_TITLE,
        'current_date': datetime.datetime.now().strftime("%d/%m/%Y")
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': f'{SITE_TITLE}: Каталог',
        'current_date': datetime.datetime.now().strftime("%d/%m/%Y"),
        'products': Product.objects.all()
    }
    return render(request, 'products/products.html', context)



