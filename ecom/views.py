import imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


#ECOM

def home(request):
    return render(request,'ecom/home.html')

def search(request):
    return render(request,'ecom/search.html')


def orders(request):
    return render(request,'ecom/orders.html')

def cart(request):
    return render(request,'ecom/cart.html')

def profile(request):
    return render(request,'ecom/profile.html')

def payment(request):
    return render(request,'ecom/payment.html')



# ACCOUNTS

def login(request):
    return HttpResponse("This is loginpage")

def signup(request):
    return HttpResponse("This is Signuppage")

def changepassword(request):
    return HttpResponse("This is Forgotpasscode  page")
