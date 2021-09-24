from django.contrib import auth
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
            # message.sucess(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm(data=request.POST)
    context = {
        'title': 'GS: Регистрация',
        'form': form
    }
    return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
    context = {
        'title': 'GS: Профиль',
        'form': UserProfileForm(instance=request.user),
        'basket': Basket.objects.filter(user=request.user)
    }
    return render(request, 'users/profile.html', context)
