import datetime
import json
import os.path

from django.shortcuts import render

SITE_TITLE = 'geeks'


def index(request):
    context = {
        'title': SITE_TITLE,
        'current_date': datetime.datetime.now().strftime("%d/%m/%Y")
    }
    return render(request, 'products/index.html', context)


def products(request):
    def readfile(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            return json.load(f)

    context = {
        'title': f'{SITE_TITLE}: Каталог',
        'current_date': datetime.datetime.now().strftime("%d/%m/%Y"),
        'products': readfile(os.path.join(os.path.dirname(__file__), 'fixtures/products.json'))
    }
    return render(request, 'products/products.html', context)


def test(request):
    context = {
        'title': 'geekshop',
        'header': 'Welcome!',
        'user': 'Demo',
        'products': [
            {'name': 'Варежки', 'price': 100, 'ispromo': 1},
            {'name': 'Вареники', 'price': 155},
            {'name': 'Пряники', 'price': 234}
        ]
    }
    return render(request, 'products/test.html', context)

