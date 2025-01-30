from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Product, Category, Supplier
from .forms import ProductForm, CategoryForm, SupplierForm
from datetime import datetime
from django.views.generic import TemplateView, DetailView,ListView, FormView

# Create your views here.
class index(TemplateView):
    template_name = 'core/index.html'

class products(TemplateView):
    template_name = 'core/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context
    
class categorys(ListView):
    model = Category
    template_name = 'core/categoryes.html'
    context_object_name = 'categoryes'

#user list view deps
class supplier(ListView):
    model = Supplier
    template_name = 'core/supplier.html'
    context_object_name = 'suppliers'

class details(DetailView):
    model = Product
    template_name = 'core/details.html'
    context_object_name = 'product'

class newProduct(FormView):
    template_name = 'core/new-product.html'
    form_class = ProductForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        product = Product()
        data = form.cleaned_data
        product.name = data['name']
        product.code = data['code']
        product.description = data['description']
        product.quantity = data['quantity']
        product.price = data['price']
        product.supplier = data['supplier']
        product.creation_date = datetime.now()

        product.save()
        product.categories.set(data['categories'])
        return redirect(self.success_url)

class newCategory(FormView):
    template_name = 'core/newcategory.html'
    form_class = CategoryForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        category = Category()
        data = form.cleaned_data

        category.name = data['name']
        category.save()
        return redirect(self.success_url)

class newSupplier(FormView):
    template_name = 'core/newsupplier.html'
    form_class = SupplierForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        supplier = Supplier()
        data = form.cleaned_data
        supplier.name = data['name']
        supplier.cnpj = data['cnpj']
        supplier.save()
        return redirect(self.success_url)