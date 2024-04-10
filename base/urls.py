from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:foo>', views.category, name='category'),
    path('product/<int:pk>', views.product, name='product'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register_user, name='register'),
    path('search/', views.search, name='search'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('categerias/', views.categorias, name='categorias'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_info/', views.update_info, name='update_info'),
]
