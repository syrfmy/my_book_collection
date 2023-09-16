from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from main.models import Product
from django.urls import reverse

def show_main(request):
    context = {
        'name': 'Muh. Syarief Mulyadi',
        'class': 'PBP E',
        'products': Product.objects.all(),
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

# Create your views here.
