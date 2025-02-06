from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Product, Category, Supplier
from .forms import ProductForm, CategoryForm, SupplierForm
from datetime import datetime
from django.views.generic import TemplateView, DetailView,ListView, FormView

# Create your views here.
class index(TemplateView):
    template_name = 'core/index.html'


class products(ListView):
    model = Product
    template_name = 'core/products.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        queryset =  super(products,self).get_queryset()
        data = self.request.GET
        search = data.get('search')
        price_min = data.get('price_min')
        price_max = data.get('price_max')

        #aplicando lookups de querys
        # LIKE do sql basicamente
        if search:
            queryset = queryset.filter(name__icontains=search) 

        # greater_than
        if price_min:
            queryset = queryset.filter(price__gte=price_min)

        # less_than
        if price_max:
            queryset = queryset.filter(price__lte=price_max)


        return queryset
    
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