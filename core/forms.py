from django import forms
from .models import Category, Supplier

class ProductForm(forms.Form):
    name = forms.CharField(label= "name", max_length=50)
    code = forms.CharField(label = "code", max_length=30)
    description = forms.CharField(label = "description", widget=forms.Textarea)
    price = forms.DecimalField(label = "price")
    categories = forms.ModelMultipleChoiceField( queryset= Category.objects.all(), widget = forms.CheckboxSelectMultiple)
    supplier = forms.ModelChoiceField( queryset= Supplier.objects.all(), label = "supplier") 

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