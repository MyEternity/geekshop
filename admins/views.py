from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
from geekshop.mixin import CustomDispatchMixin
from products.models import Product, ProductCategory
from users.models import User


def index(request):
    return render(request, 'admins/admin.html')


class ProductCreateView(CreateView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-create.html'
    fields = ['name', 'description', 'price', 'quantity', 'category']
    success_url = reverse_lazy('admins:products_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Панель управления / Создание товара'
        return context


class ProductsListView(ListView):
    model = Product
    template_name = 'admins/admin-products-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['title'] = 'Панель управления / Товары'
        return context


class ProductUpdateView(UpdateView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    fields = ['name', 'description', 'price', 'quantity', 'category']
    success_url = reverse_lazy('admins:products_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Панель управления / Редактирование продукции'
        return context


class ProductDeleteView(DeleteView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:products_list')


class ProductCategoriesCreateView(CreateView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-create.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('admins:categories_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoriesCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Панель управления / Создание категории'
        return context


class ProductCategoriesListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-categories-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoriesListView, self).get_context_data(**kwargs)
        context['title'] = 'Панель управления / Категории товаров'
        return context


class ProductCategoriesUpdateView(UpdateView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('admins:categories_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoriesUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Панель управления / Редактирование категорий'
        return context


class ProductCategoriesDeleteView(DeleteView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    success_url = reverse_lazy('admins:categories_list')


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Панель управления / Пользователи'
        return context


class UserCreateView(CreateView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Панель управления / Регистрация пользователя'
        return context


class UserUpdateView(UpdateView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Панель управления / Редактирование пользователя'
        return context


class UserDeleteView(DeleteView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admin_users')

    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
