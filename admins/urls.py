from django.urls import path
from .views import index, UserUpdateView, UserDeleteView, UserCreateView, UserListView

app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('users-create/', UserCreateView.as_view(), name='admin_users_create'),
    path('users-update/<pk>', UserUpdateView.as_view(), name='admin_users_update'),
    path('users-delete/<pk>', UserDeleteView.as_view(), name='admin_users_delete'),
]
