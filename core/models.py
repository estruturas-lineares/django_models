from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField('name',max_length=200)
    code = models.CharField('code', max_length=200, unique=True)
    description = models.TextField('description',blank=True)
    price = models.DecimalField('price',max_digits=10, decimal_places = 2)
    creation_date = models.DateTimeField('date',auto_now_add=True)