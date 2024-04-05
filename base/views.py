from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html',{'products': products})

def carrinho(request):
    return render(request, 'carrinho.html')

def detalhes(request):
    pass

def pedidos(request):
    return render(request, 'pedidos.html')

def pedido(request):
    pass

# Ofertas
def ofertas(request):
    products = Product.objects.filter(is_sale=True)
    return render(request, 'oferta.html', {'products': products})

# Pagina Categorias
def categorias(request):
    return render(request, 'categorias.html', {'category': category})

# Category
def category(request,foo):
    foo = foo.replace('-',' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render (request, 'category.html',{'products':products, 'category':category})

    except: 
        return redirect('home')




def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso")
            return redirect('home')
        else:
                messages.error(request, "Erro ao autenticar o usuário após o cadastro")
                return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})

# Login
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso")
            return redirect('home')
        else:
            messages.error(request, "Nome de usuário ou senha inválidos")
            return redirect('login_user')
    else:
        return render(request, 'login.html', {})
# Logout
def logout_user(request):
    logout(request)
    messages.success(request, "Conta desconectada")
    return redirect('home')


# Detalhes Produto
def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})
# Pesquisa
def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched = Product.objects.filter(name__icontains=searched)
        if not searched:
            messages.success(request, 'Produto não existe')
            return render(request, 'search.html', {})

        return render(request, 'search.html', {'searched':searched})
    else:
        return render(request, 'search.html', {})