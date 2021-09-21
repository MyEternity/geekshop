from django.shortcuts import render


from users.forms import UserLoginForm
# Create your views here.


def login(request):
    form = UserLoginForm()
    context = {
        'title': 'GS: Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    context = {
        'title': 'GS: Регистрация'
    }
    return render(request, 'users/register.html', context)
