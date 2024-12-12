from django.shortcuts import render
from .models import Product, Category,Supplier

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