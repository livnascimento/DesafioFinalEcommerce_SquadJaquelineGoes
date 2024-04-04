from django.contrib import admin
from django.urls import path
from base.views import home, carrinho, pedidos, category, search, product, logout_user, register_user, login_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('carrinho/', carrinho),
    path('pedidos/', pedidos),
    path('category/<str:foo>', category, name='category'),
    path('product/<int:pk>', product, name='product'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('register/', register_user, name='register'),
    path('search/', search, name='search'),
]
