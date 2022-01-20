from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('cart/',views.cart,name='cart'),
    path('orders/',views.orders,name='orders'),
    path('profile/',views.profile,name='profile'),
    path('payment/',views.payment,name='payment'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('forgotpassword/',views.changepassword,name='changepassword'),
]
