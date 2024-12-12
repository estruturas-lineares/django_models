from django.db import models

class Category(models.Model):
    name = models.CharField('name',max_length=200)
    creation_date = models.DateTimeField('date',auto_now_add=True)
    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField('name',max_length=200)
    cnpj =  models.CharField('cnpj',max_length=14, unique=True)
    creation_date = models.DateTimeField('date',auto_now_add=True)
    def __str__(self):
        return self.name
# Create your models here.
class Product(models.Model):
    name = models.CharField('name',max_length=200)
    code = models.CharField('code', max_length=200, unique=True)
    description = models.TextField('description',blank=True)
    price = models.DecimalField('price',max_digits=10, decimal_places = 2)
    creation_date = models.DateTimeField('date',auto_now_add=True)
    categories = models.ManyToManyField(Category)
    supplier = models.ForeignKey(Supplier, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name