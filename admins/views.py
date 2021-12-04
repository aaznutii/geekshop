from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategotyAdminForm, ProductAdminForm
from auth_app.models import User
from products.models import Product, ProductCategory


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)

def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Geekshop - Админ | Регистрация',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, pk):
    user_select = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST,instance=user_select,files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form':form,
        'user_select':user_select
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        user.is_active=False
        user.save()
    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_category(request):
    context = {
        'categories': ProductCategory.objects.all()
    }
    return render(request, 'admins/admin-category-read.html', context)

def admin_category_create(request):
    if request.method == 'POST':
        form = CategotyAdminForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category'))
    else:
        form = CategotyAdminForm()
    context = {
        'title': 'Geekshop - Админ | Категории',
        'form': form
    }
    return render(request, 'admins/admin-category-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_update(request, pk):
    category_select = ProductCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategotyAdminForm(data=request.POST,instance=category_select)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = CategotyAdminForm(instance=category_select)
    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form':form,
        'category_select':category_select
    }
    return render(request, 'admins/admin-category-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_delete(request, pk):
    if request.method == 'POST':
        category = ProductCategory.objects.get(pk=pk)
        category.delete()
    return HttpResponseRedirect(reverse('admins:admin_category'))


@user_passes_test(lambda u: u.is_superuser)
def admin_product(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'admins/admin-product-read.html', context)

def admin_product_create(request):
    if request.method == 'POST':
        form = ProductAdminForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_product_create'))
    else:
        form = ProductAdminForm()
    context = {
        'title': 'Geekshop - Админ | Продукты',
        'form': form
    }
    return render(request, 'admins/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_update(request, pk):
    product_select = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductAdminForm(data=request.POST,instance=product_select)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_product'))
    else:
        form = ProductAdminForm(instance=product_select)
    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form':form,
        'product_select':product_select
    }
    return render(request, 'admins/admin-product-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_delete(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        product.delete()
    return HttpResponseRedirect(reverse('admins:admin_product'))
