from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import FormView

from .models import Product, ProductCategory

SITE_TITLE = 'geeks'


class IndexView(FormView):
    form_class = FormView
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = SITE_TITLE
        return context


# class ProductsView(FormView):
#     form_class = FormView
#     template_name = 'products/products.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(ProductsView, self).get_context_data(**kwargs)
#         context['title'] = SITE_TITLE
#
#         if self.request.code is None:
#             selected_products = Product.objects.all()
#         else:
#             selected_products = Product.objects.filter(category_id=self.request.code)
#
#         paginator = Paginator(selected_products, per_page=3)
#         try:
#             pp = paginator.page(self.request.page_id)
#         except PageNotAnInteger:
#             pp = paginator.page(1)
#         except EmptyPage:
#             pp = paginator.page(paginator.num_pages)
#
#         context['products'] = pp
#         context['categories'] = ProductCategory.objects.all()
#         return context


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
