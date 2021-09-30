from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from basket.models import Basket
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm


# Create your views here.


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
        else:
            form = UserLoginForm(data=request.POST)
    else:
        form = UserLoginForm()
    context = {
        'title': 'GS: Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm(data=request.POST)
    context = {
        'title': 'GS: Регистрация',
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


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
