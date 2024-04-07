from django.contrib import admin
from django.urls import path
from base.views import home, carrinho, pedidos, category, search, product, user_logout, register_user, login_user, ofertas, categorias
from django.conf.urls.static import static
from .import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('carrinho/', carrinho),
    path('pedidos/', pedidos),
    path('category/<str:foo>', category, name='category'),
    path('product/<int:pk>', product, name='product'),
    path('login/', login_user, name='login_user'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', register_user, name='register'),
    path('search/', search, name='search'),
    path('ofertas/', ofertas, name='ofertas'),
    path('categerias/', categorias, name='categorias')
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

