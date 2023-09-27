from django.forms import ModelForm
from main.models import Product
from django import forms

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name","author","status","amount", "description"]


class AddStockForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Tambah Stok')

class DeleteProductForm(forms.Form):
    pass  # Form ini hanya memerlukan tombol submit, tidak ada field tambahan
