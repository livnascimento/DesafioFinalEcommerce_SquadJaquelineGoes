from django.db import models
from base.classes import Item
import datetime


# Categoria dos produtos
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural ='categories'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/product/')

  

    def __str__(self):
        return self.name


class Carrinho(models.Model):
    produtos = models.JSONField()

class Pedidos(models.Model):
    data = models.DateTimeField(auto_now_add=True)
  

# Clientes
class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)


    def __str__(self):
        return f'{self.name}'

