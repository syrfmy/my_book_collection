import datetime
import json
from django.shortcuts import render, redirect, get_object_or_404 
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from main.forms import ProductForm, AddStockForm, DeleteProductForm
from main.models import Product
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')

def show_main(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'class': 'PBP E',
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    context = {'form': form}
    return render(request, "create_product.html", context)

def show_book(request):
    context = {
        'products':Product.objects.all()
    }
    return render(request, "show_book.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type= "application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
     

def change_amount(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'class': 'PBP E',
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "change_amount.html", context)

def add_stock(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = AddStockForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            product.stock += quantity
            product.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = AddStockForm()

    return render(request, 'add_stock.html', {'product': product, 'form': form})

def reduce_stock(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        if product.stock > 0:
            product.stock -= 1
            product.save()
        return redirect('product_detail', product_id=product.id)

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        return redirect('product_list')  # Ganti dengan URL yang sesuai

    form = DeleteProductForm()
    return render(request, 'delete_product.html', {'product': product, 'form': form})