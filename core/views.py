from django.shortcuts import render, redirect
from .models import Product, Category, Supplier
from .forms import ProductForm, CategoryForm, SupplierForm
from datetime import datetime

# Create your views here.
def index (request):
    return render(request,"core/index.html")

def products(request):
    products_model = Product.objects.all()
    context = {'products': products_model}
    return render(request, "core/products.html", context)

def categorys(request):
    categorys_model = Category.objects.all()
    context = {'categoryes': categorys_model}
    return render(request, "core/categoryes.html", context)

def supplier(request):
    suppliers = Supplier.objects.all()
    context = {'suppliers': suppliers}
    return render(request, "core/supplier.html", context)

def details(request, product_id):
    prodcut = Product.objects.get(id = product_id)  
    context = {'product': prodcut}
    return render(request, "core/details.html", context)

def newProduct(request):
    if (request.method == 'GET'):
        form = ProductForm()
        return render (request, 'core/new-product.html', {'form': form})
    form = ProductForm(request.POST)
    if form.is_valid():
        product = Product()
        data = form.cleaned_data
        product.name = data['name']
        product.code = data['code']
        product.description = data['description']
        product.price = data['price']
        product.supplier = data['supplier']
        product.creation_date = datetime.now()

        product.save()
        product.categories.set(data['categories'])
        return redirect('products')
    else:
        return render(request, 'core/new-product.html', {'form': form})
    
def newCategory(request):
    if request.method == 'GET':
        form = CategoryForm()
        return render(request, 'core/newcategory.html', {'form': form})
    
    form = CategoryForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        category = Category()
        category.name = data['name']
        category.save()
        return redirect('categoryes')
    else:
        return render(request, 'core/newcategory.html', {'form': form})
    
def newSupplier(request):
    if request.method == 'GET':
        form = SupplierForm()
        return render(request, 'core/newsupplier.html', {'form': form})

    form = SupplierForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        supplier = Supplier()
        supplier.name = data['name']
        supplier.cnpj = data['cnpj']
        supplier.save()
        return redirect('supplier')
    else:
        return render (request, 'core/newsupplier.html', {'form': form})