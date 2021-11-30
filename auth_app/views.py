from django.shortcuts import render
from django.contrib import auth, messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


# Create your views here.
from django.urls import reverse

from auth_app.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from baskets.models import Basket


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            # Добавлена проверка поскольку при выходе user возвращает NonType
            try:
                if user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('index'))
            except AttributeError:
                pass
                # return render(request, 'products/index.html')
        else:
            messages.error(request, f'Введите корректные данные.')
    else:
        form = UserLoginForm()
    context = {
        'title': 'Geekshop | Авторизация',
        'form': form
    }
    return render(request, 'login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались.')
            return HttpResponseRedirect(reverse('auth_app:login'))
        else:
            messages.error(request, f'Ошибочные данные.')
    else:
        form = UserRegisterForm()
    context = {
        'title': 'Geekshop | Регистрация',
        'form': form}
    return render(request, 'register.html', context)


def logout(request):
    auth.logout(request)
    return render(request, 'products/index.html')


@login_required
def profile(request):
    if request.method == 'POST':
       form = UserProfileForm(instance=request.user,data=request.POST,files=request.FILES)
       if form.is_valid():
           messages.set_level(request, messages.SUCCESS)
           messages.success(request, 'Изменения сохранены', extra_tags='success')
           form.save()
       else:
           messages.set_level(request, messages.ERROR)
           messages.error(request, 'Ошибка формы', extra_tags='error')
    total_quantity = sum(bask.quantity for bask in Basket.objects.filter(user=request.user))
    total_sum = sum(bask.sum() for bask in Basket.objects.filter(user=request.user))
    context = {
        'title': 'Geekshop | Профайл',
        'form' : UserProfileForm(instance=request.user),
        'baskets': Basket.objects.filter(user=request.user),
        'total_quantity': total_quantity,
        'total_sum': total_sum
    }
    return render(request, 'profile.html', context)
