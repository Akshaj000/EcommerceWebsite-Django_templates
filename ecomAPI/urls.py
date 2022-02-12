from django.contrib import admin
from django.urls import path
from .import views
from rest_framework.authtoken import views as authview


urlpatterns = [
    path('', views.apiOverview,name="api-overview"),
    path('customer-list/',views.customerList,name="customer-list"),
    path('customer-detail/<str:customerid>/',views.customerDetail,name="customer-detail"),
    path('customer-add/', views.addCustomer,name="customer-add"),
    path('customer-update/<str:customerid>/',views.updateCustomer,name="customer-update"),
    path('customer-delete/<str:customerid>/', views.deleteCustomer,name="customer-delete"),  

    path('product-list/',views.productList,name="product-list"),
    path('product-detail/<str:productid>/',views.productDetail,name="product-detail"),
    path('product-create/',views.createProduct,name="product-create"),
    path('product-update/<str:productid>/',views.updateProduct,name="product-update"),
    path('product-delete/<str:productid>/',views.deleteProduct,name="product-delete"),

    path('category-list/',views.categoryList,name="category-list"),
    path('category-add/',views.addCategory,name="category-add"),
    path('category-remove/<str:categoryid>/',views.removeCategory,name="category-remove"),

    path('cart-list/<str:customerid>/',views.cartList,name="cart-list"),
    path('cart-detail/<str:cartid>/',views.cartDetail,name="cart-detail"),
    path('cart-add/<str:customerid>/<str:productid>/',views.addCart,name="cart-add"),
    path('cart-remove/<str:customerid>/<str:productid>/',views.removeCart,name="cart-remove"),
    path('cart-update/<str:customerid>/<str:productid>/',views.updateCart,name="cart-update"),

    path('order-list/<str:customerid>/',views.orderList,name="order-list"),
    path('order-detail/<int:orderid>/',views.orderDetail,name="order-detail"),
    path('order-add/',views.addOrder,name="order-add"),
    path('order-remove/<int:orderid>/',views.removeOrder,name="order-remove"),
    path('order-update/<int:orderid>/',views.updateOrder,name="order-update"),

]