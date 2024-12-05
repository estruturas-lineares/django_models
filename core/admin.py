from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin (admin.ModelAdmin):
    list_display = ['name', 'code', 'price', 'creation_date']
    list_filter = ['creation_date']
    search_fields = ['code', 'name',]
    ordering = ['-creation_date',]

admin.site.register(Product, ProductAdmin)