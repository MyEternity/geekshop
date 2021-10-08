from django.urls import path

from .views import index, UserUpdateView, UserDeleteView, UserCreateView, UserListView, ProductsListView, \
    ProductCategoriesListView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<pk>', UserDeleteView.as_view(), name='admin_users_delete'),
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('product-create/', ProductsListView.as_view(), name='product_create'),
    path('product-update/', ProductsListView.as_view(), name='product_update'),
    path('product-delete/', ProductsListView.as_view(), name='product_delete'),
    path('categories/', ProductCategoriesListView.as_view(), name='categories_list'),
    path('category-create/', ProductCategoriesListView.as_view(), name='category_create'),
    path('category-update/', ProductCategoriesListView.as_view(), name='category_update'),
    path('category-delete/', ProductCategoriesListView.as_view(), name='category_delete'),
]
