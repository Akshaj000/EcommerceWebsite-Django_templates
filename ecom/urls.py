from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('search/',views.search,name='search'),
    path('product/<str:name>/',views.productdetails,name='productdetails'),
    path('cart/',views.cart,name='cart'),
    path('savetocart/<str:pname>/',views.addtocart,name='addtocart'),
    path('removefromcart/<str:pname>/',views.removefromcart,name='removefromcart'),
    path('orders/',views.orders,name='orders'),
    path('addproduct/',views.addproducts,name='addproducts'),
    path('addcategory/',views.addcategory,name='addcategory'),
    path('editproduct/<str:pname>/',views.editproducts,name='editproducts'),
    path('deleteproduct/<str:pname>/',views.deleteproducts,name='deleteproducts'),

    path('profile/',views.profile,name='profile'),
    path('editprofile/',views.editprofile,name='editprofile'),


    path('payment/<str:payment_id>/',views.payment,name='payment'),

    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('forgotpassword/',views.changepassword,name='changepassword'),
]
