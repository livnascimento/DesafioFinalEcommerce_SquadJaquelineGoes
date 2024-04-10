from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import UserForm
from .forms import  UpdateUserForm, ChangePasswordForm, UserInfoForm

from payment.forms import ShippingForm
from payment.models import ShippingAddress

from django import forms
from django.db.models import Q
import json
from cart.cart import Cart


def home(request):
    products = Product.objects.all()
    for product in products:
        product.stars = range(product.rating) if product.rating else range(5)
    return render(request, 'home.html',{'products': products})

# Atualizar pagamento
def update_info(request):
	if request.user.is_authenticated:
		# Get Current User
		current_user = Profile.objects.get(user__id=request.user.id)
		# Get Current User's Shipping Info
		shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
		
		# Get original User Form
		form = UserInfoForm(request.POST or None, instance=current_user)
		# Get User's Shipping Form
		shipping_form = ShippingForm(request.POST or None, instance=shipping_user)		
		if form.is_valid() or shipping_form.is_valid():
			# Save original form
			form.save()
			# Save shipping form
			shipping_form.save()

			messages.success(request, "Your Info Has Been Updated!!")
			return redirect('home')
		return render(request, "update_info.html", {'form':form, 'shipping_form':shipping_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')

# Ofertas
def ofertas(request):
    products = Product.objects.filter(is_sale=True)
    return render(request, 'oferta.html', {'products': products})

# Pagina Categorias
def categorias(request):
    return render(request, 'categorias.html', {'category': category})

# Categoria
def category(request,foo):
    foo = foo.replace('-',' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render (request, 'category.html',{'products':products, 'category':category})

    except: 
        return redirect('home')

# Atualizar Senha
def update_password(request):
	if request.user.is_authenticated:
		current_user = request.user
		# Did they fill out the form
		if request.method  == 'POST':
			form = ChangePasswordForm(current_user, request.POST)
			# Is the form valid
			if form.is_valid():
				form.save()
				messages.success(request, "Your Password Has Been Updated...")
				login(request, current_user)
				return redirect('update_user')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)
					return redirect('update_password')
		else:
			form = ChangePasswordForm(current_user)
			return render(request, "update_password.html", {'form':form})
	else:
		messages.success(request, "You Must Be Logged In To View That Page...")
		return redirect('home')

# Atualizar nome
def update_user(request):
	if request.user.is_authenticated:
		current_user = User.objects.get(id=request.user.id)
		user_form = UpdateUserForm(request.POST or None, instance=current_user)

		if user_form.is_valid():
			user_form.save()

			login(request, current_user)
			messages.success(request, "User Has Been Updated!!")
			return redirect('home')
		return render(request, "update_user.html", {'user_form':user_form})
	else:
		messages.success(request, "You Must Be Logged In To Access That Page!!")
		return redirect('home')

# Cadastro
def register_user(request):
    template_name = 'register.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save()
            f.set_password(f.password)
            f.save()
            messages.success(request, 'Usuário cadastrado com sucesso.')
            return redirect('login_user')
    form = UserForm()
    context['form'] = form
    return render(request, template_name, context)

# Login
def login_user(request):
    template_name = 'login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            current_user = Profile.objects.get(user_id=request.user.id)
            saved_cart = current_user.old_cart
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)
                for key, value in converted_cart.item():
                      cart.db_add(product=key, quantity=value)

            messages.success(request, ('Login realizado com sucesso'))
            return redirect('home')
        else:
            messages.success(request, ('Aconteceu algum erro, por favor, tente novamente'))
            return redirect('login_user')

    return render(request, template_name, {})
# Logout
def user_logout(request):
    logout(request)
    messages.success(request, 'Você saiu do sistema.')
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