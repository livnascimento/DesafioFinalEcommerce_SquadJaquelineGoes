from django.contrib import admin
from django.urls import path
from base.views import home, carrinho, pedidos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('carrinho/', carrinho),
    path('pedidos/', pedidos)
]
