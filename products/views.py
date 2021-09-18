from django.shortcuts import render


def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')


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

