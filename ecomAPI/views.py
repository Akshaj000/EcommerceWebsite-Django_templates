from urllib import request
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from urllib3 import Retry
from ecom.models import*
from .serializers import*

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Customer List' : '/customer-list/',
        'Customer Detail' : '/customer-detail/<str:customerid>/',
        'Customer Add'  :  '/Customer-add/',
        'Customer Update': '/customer-update/<str:customerid>/',
        'Customer Delete' : '/customer-delete/<str:customerid>/' ,  

        'Product List' : '/product-list/',
        'Product Detail' :  '/product-detail/<str:productid>/',
        'Create Product' : '/product-create/',
        'Update Product' : '/product-update/<str:productid>/',
        'Delete Product' : '/product-delete/<str:productid>/',

        'Category List':'/category-list/',
        'Add Category':'/category-add/',
        'Remove Category':'/category-remove/<str:categoryid>/',

        'Cart List' : '/cart-list/<str:customerid>/',
        'Cart Detail' : '/cart-detail/<str:cartid>/',
        'Add to cart'  : '/cart-add/<str:customerid>/<str:productid>/',
        'Remove from cart' : '/cart-remove/<str:customerid>/<str:productid>/',
        'Update cart' : '/cart-update/<str:customerid>/<str:productid>/',

        'Order List':'/order-list/<str:customerid>/',
        'Order Detail':'/order-detail/<str:orderid>/',
        'Place Order' : '/order-add/',
        'Delete Order' : '/order-remove/<str:orderid>/',
        'Update Order' : '/order-update/<str:orderid>/',
        
    } 
    return Response(api_urls)

#Customer--------------------------------------------------------------------

@api_view(['GET'])
def customerList(request):
    customers = Customer.objects.all()
    serialiser = CustomerSerializer(customers, many=True)
    return Response(serialiser.data)

@api_view(['GET'])
def customerDetail(request,customerid):
    customer = Customer.objects.get(id=customerid)
    serialiser = CustomerSerializer(customer, many=False)
    return Response(serialiser.data)

@api_view(['POST'])
def addCustomer(request):
    serialiser = CustomerSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

@api_view(['POST'])
def updateCustomer(request,customerid):
    customer = Customer.objects.get(id=customerid)
    serialiser = CustomerSerializer(instance=customer,data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

@api_view(['DELETE'])
def deleteCustomer(request,customerid):
    customer = Customer.objects.get(id=customerid)
    customer.delete();
    return Response("Customer successfully removed!")

#Product--------------------------------------------------------------------

@api_view(['GET'])
def productList(request):
    products = Product.objects.all()
    serialiser = ProductSerializer(products, many=True)
    return Response(serialiser.data)

@api_view(['GET'])
def productDetail(request,productid):
    product = Product.objects.get(id=productid)
    serialiser = ProductSerializer(product, many=False)
    return Response(serialiser.data)

@api_view(['POST'])
def createProduct(request):
    serialiser = ProductSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

@api_view(['POST'])
def updateProduct(request,productid):
    product = Product.objects.get(id=productid)
    serialiser = ProductSerializer(instance=product,data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

@api_view(['DELETE'])
def deleteProduct(request,productid):
    product = ProductSerializer.objects.get(id=productid)
    product.delete()
    return Response("Product successfully deleted!")


#Category--------------------------------------------------------------------

@api_view(['GET'])
def categoryList(request):
    category = Category.objects.all()
    serialiser = CategorySerializer(category, many=True)
    return Response(serialiser.data)

@api_view(['POST'])
def addCategory(request):
    serialiser = CategorySerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

@api_view(['DELETE'])
def removeCategory(request,categoryid):
    category = Category.objects.get(id=categoryid)
    category.delete()
    return Response("Category successfully deleted!")

#Cart--------------------------------------------------------------------------

@api_view(['GET'])
def cartList(request,customerid):
    try:
        thiscustomer = Customer.objects.get(id=customerid)
        try:
            cart = Cart.objects.filter(customer=thiscustomer)
            serialiser = CartSerializer(cart, many=True)
            return Response(serialiser.data)
        except:
            return Response("Cart is empty!")
    except:
        return Response("Customer does not exist!")

@api_view(['GET'])
def cartDetail(request,cartid):
    cart = Cart.objects.get(id=cartid)
    serialiser = ProductSerializer(cart, many=False)
    return Response(serialiser.data)

@api_view(['POST','GET'])
def addCart(request,customerid,productid,force):
    try:
        product = Product.objects.get(id=productid)
        customer = Customer.objects.get(id=customerid)
        cart = Cart.objects.get(product=product,customer=customer)
        cart.count+=1
        cart.save()
        return Response("count incremented!")
    except:
        serialiser = CartSerializer(data=request.data)
        if serialiser.is_valid():
            serialiser.save()
        return Response(serialiser.data)

@api_view(['DELETE','GET'])
def removeCart(request,customerid,productid):
    try:
        product = Product.objects.get(id=productid)
        customer = Customer.objects.get(id=customerid)
        cart = Cart.objects.get(product=product,customer=customer)
        if cart.count == 0:
            cart.delete()
            return Response("Cart successfully deleted!")
        else:
            cart.count-=1
            cart.save()
            return Response("count decremented!")
    except:
        return Response("Cart doesnt exist")

@api_view(['POST'])
def updateCart(request,customerid,productid):
    try:
        product = Product.objects.get(id=productid)
        customer = Customer.objects.get(id=customerid)
        cart = Cart.objects.get(product=product,customer=customer)
        serialiser = CartSerializer(instance=cart,data=request.data)
        if serialiser.is_valid():
            serialiser.save()
        return Response(serialiser.data)
    except:
        return Response("Cart doesnt exist")

#Orders------------------------------------------------------------------------------

@api_view(['GET'])
def orderList(request,customerid):
    try:
        thiscustomer = Customer.objects.get(id=customerid)
        try:
            order = Order.objects.filter(customer=thiscustomer)
            serialiser = OrderSerializer(order, many=True)
            return Response(serialiser.data)
        except:
            return Response("Cart is empty!")
    except:
        return Response("Customer does not exist!")

@api_view(['GET'])
def orderDetail(request,orderid):
    order = Order.objects.get(id=orderid)
    serialiser = OrderSerializer(order, many=False)
    return Response(serialiser.data)

@api_view(['POST','GET'])
def addOrder(request): 
    serialiser = OrderSerializer(data=request.data)
    if serialiser.is_valid():
        serialiser.save()
    return Response(serialiser.data)

@api_view(['DELETE'])
def removeOrder(request,orderid):
    try:
        order = Product.objects.get(id=orderid)
        order.delete()
        return Response("Order successfully deleted!")
  
    except:
        return Response("Order doesnt exist")


@api_view(['POST'])
def updateOrder(request,orderid):
    try:
        order = Order.objects.get(id=orderid)
        serialiser = OrderSerializer(instance=order,data=request.data)
        if serialiser.is_valid():
            serialiser.save()
        return Response(serialiser.data)
    except:
        return Response("Order doesnt exist")