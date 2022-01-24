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

    path('invoice/<int:pk>/',views.invoice,name='invoice'),

    path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),


    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('forgotpassword/',views.changepassword,name='changepassword'),
]
