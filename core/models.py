from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField('category_name', max_length=200)
    creation_date = models.DateTimeField('date',auto_now_add=True)
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField('supplier_name', max_length=200)
    cnpj = models.CharField('cnpj', max_length=14, unique=True)
    creation_date = models.DateTimeField('date',auto_now_add=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField('name',max_length=200)
    code = models.CharField('code', max_length=200, unique=True)
    description = models.TextField('description',blank=True)
    price = models.DecimalField('price',max_digits=10, decimal_places = 2)
    creation_date = models.DateTimeField('date',auto_now_add=True)

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, related_name='products')

    def __str__(self):
        return self.name
