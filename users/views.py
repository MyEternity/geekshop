from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, FormView

from basket.models import Basket
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm

# Create your views here.
from users.models import User


class LoginListView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    # title = 'Авторизация'
    # success_url = reverse_lazy('index')


# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#         else:
#             form = UserLoginForm(data=request.POST)
#     else:
#         form = UserLoginForm()
#     context = {
#         'title': 'GS: Авторизация',
#         'form': form
#     }
#     return render(request, 'users/login.html', context)


class RegisterListView(FormView):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect(self.success_url)
        messages.success(request, form.error_messages)
        return redirect(self.success_url)


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрировались!')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegisterForm(data=request.POST)
#     context = {
#         'title': 'GS: Регистрация',
#         'form': form
#     }
#     return render(request, 'users/register.html', context)


class Logout(LogoutView):
    template_name = 'products/index.html'


# @login_required
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))


def total_sale(self):
    total = Basket.objects.aggregate(TOTAL=Sum('amount'))['TOTAL']
    return total


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно сохранены.')
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        'title': 'GS: Профиль',
        'form': form,
        'basket': Basket.objects.filter(user=request.user),
    }
    return render(request, 'users/profile.html', context)
