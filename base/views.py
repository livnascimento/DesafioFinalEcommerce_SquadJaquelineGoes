from django.http import HttpResponse
from django.shortcuts import render
from base.models import Produtos

def home(request):
    produtos = Produtos.objects.all()
    return render(request, 'home.html', {'produtos': produtos})

def carrinho(request):
    return render(request, 'carrinho.html')

def detalhes(request):
    pass

def pedidos(request):
    return render(request, 'pedidos.html')

def pedido(request):
    pass