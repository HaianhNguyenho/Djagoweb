from django.contrib import admin
from django.urls import path
from .import views
app_name="app"

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),
    path('search/', views.search, name="search"),
    path('detail/', views.detail, name="detail"),
    path('logout/', views.logoutPage, name="logout"),
    path('contact/', views.contact, name="contact"),
    path('cart/', views.cart, name="cart"),
    path('checkout/',views.checkout, name="checkout"),
    path('add_cart/',views.addgh, name="add_cart"),
]