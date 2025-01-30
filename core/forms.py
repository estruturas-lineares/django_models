from django import forms
from .models import Category, Supplier
from django.core.validators import ValidationError


class ProductForm(forms.Form):
    name = forms.CharField(label= "name", max_length=50, min_length=3)
    code = forms.CharField(label = "code", max_length=30)
    description = forms.CharField(label = "description", widget=forms.Textarea)
    price = forms.DecimalField(label = "price")
    quantity = forms.IntegerField(label = "quantity")
    categories = forms.ModelMultipleChoiceField( queryset= Category.objects.all(), widget = forms.CheckboxSelectMultiple)
    supplier = forms.ModelChoiceField( queryset= Supplier.objects.all(), label = "supplier") 

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("O preço deve ser maior que zero")
        return price
    
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 0:
            raise ValidationError("Quantidade deve ser maior ou igual a zero")
        return quantity
    
    def clean_code(self):
        code = self.cleaned_data.get('code')
        if not code.isalnum():
            raise ValidationError("Código não poder conter espaços ou caracteres especiais")
        return code

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name'] 
        labels = {'name': 'Nome categoria'} 

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'cnpj']
        labels = {'name': 'Nome do fornecedor', 'cnpj': 'CNPJ'}