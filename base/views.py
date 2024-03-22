from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def carrinho(request):
    return render(request, 'carrinho.html')

def detalhes(request):
    pass

def pedidos(request):
    return render(request, 'pedidos.html')

def pedido(request):
    pass