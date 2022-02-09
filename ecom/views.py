import imp
from itertools import count, product
from pyexpat.errors import messages
from unicodedata import category
from urllib import response
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse
from pkg_resources import NullProvider
from .models import*
from .forms import*
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout, update_session_auth_hash
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from decimal import Decimal
from django.views.generic import TemplateView

# Create your views here.

#ECOM

def seperaterowandcolumn(object):
    list = []
    for i in object:
        if i not in list:
            list.append(i)
    nested_list = []
    nested_list.append([])
    count = 0
    j=0
    for i in list:
        nested_list[j].append(i)
        count+=1
        if count%3==0:
            nested_list.append([])
            j+=1
    return nested_list

def home(request):
    products = Product.objects.all()
    nested_list = seperaterowandcolumn(products)
    context = {'products':nested_list}
    return render(request,'ecom/home.html',context)

def productdetails(request,name):
    product = get_object_or_404(Product, name = name)
    return render(request,'ecom/productdetails.html',{'product':product})

def search(request):
    if 'q' in request.GET and request.GET['q']:
        products = Product.objects.all()
        nested_list = seperaterowandcolumn(products)
        if str('q').isalnum:
            q = request.GET['q']
            products = Product.objects.filter(Q(name__contains=q)|Q(category__categoryname__contains=q))
            if len(products)<=0:
                context = {'products':nested_list,'error':'Item not found!'}
                return render (request,'ecom/search.html', context)
            nested_list = seperaterowandcolumn(products)
            context = {'products':nested_list}
            return render(request, 'ecom/search.html',context)
        else:
            context = {'products':nested_list,'error':'Item not found!'}
            return render (request,'ecom/search.html', context)
    else:
        return redirect('home')

def orders(request):
    if request.user.is_authenticated:
        Orders = Order.objects.all()
        orders = []
        for object in Orders:
            try:
                if str(object.customer.name) == str(request.user):
                    orders.append(object)
            except:
                continue
        return render(request,'ecom/orders.html',{'orders':orders, 'length':len(orders)})
    
    else:
        return redirect('home')


def addtocart(request, pname):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, name = pname)
        customer = Customer.objects.get(name=str(request.user))
        try:
            cart = Cart(name = str(product.name)+str(customer.name),product  = product, customer = customer, count = 1)
            cart.save()
        except:
            cart = Cart.objects.get(product = product, customer=customer)
            cart.count += 1 
            cart.save()
        return redirect('cart')
    else:
        return redirect('login')

def removefromcart(request,pname):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, name = pname)
        customer = Customer.objects.get(name=str(request.user))
        cart = Cart.objects.get(product = product, customer=customer)
        cart.count -= 1 
        cart.save()
        if cart.count <= 0:
            cart.delete()
        return redirect('cart')
    else:
        return redirect('login')


def cart(request):
    if request.user.is_authenticated:
        tp = 0;
        cart = Cart.objects.all()
        cartlist = []
        for cartobject in cart:
            if str(cartobject.customer.name).strip() == str(request.user).strip():
                tp += cartobject.totalprice()
                cartlist.append(cartobject)
        
        length = len(cartlist)
        carts = seperaterowandcolumn(cartlist)
        return render(request,'ecom/cart.html',{'carts':carts,'totalprice':tp, 'length':length})
    else:
        return redirect('login')

def addproducts(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = ProductForm(data=request.POST,files=request.FILES)
                if form.is_valid():
                    product = form.save(commit=False)
                    product.date_created = timezone.now()
                    product.save()
                    product.category.set(form.cleaned_data.get("category"))
                    form.save_m2m()
                    return redirect('home')
            else:
                form = ProductForm()
            return render(request, 'ecom/productform.html', {'form': form})

        else:
            return redirect('home')

    else:
        return redirect('login')

def addcategory(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            if request.method == "POST":
                form = CategoryForm(data=request.POST)
                if form.is_valid():
                    cat = form.save(commit=False)
                    cat.save()
                    return redirect('home')
            else:
                form = CategoryForm()
            return render(request, 'ecom/categoryform.html', {'form': form})

        else:
            return redirect('home')

    else:
        return redirect('login')

def editproducts(request,pname):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            product = get_object_or_404(Product, name=pname)
            if request.method == "POST":
                form = ProductForm(data=request.POST,files=request.FILES,instance=product)
                if form.is_valid():
                    product = form.save(commit=False)
                    product.date_created = timezone.now()
                    product.save()
                    product.category.set(form.cleaned_data.get("category"))
                    form.save_m2m()
                    return redirect('productdetails', name=product.name)
            
            else:
                form = ProductForm(instance=product)
            return render(request, 'ecom/productform.html', {'form': form})

        else:
            return redirect('home')

    else:
        return redirect('login')

def deleteproducts(request,pname):
    products = Product.objects.get(name=pname)
    try:
        cart  = Cart.objects.get(product=products)
        cart.delete()
    except:
        pass
    products.delete()
    return redirect('home')

# PAYMENT-------------------------------------------------------------------------------------------------------------------------------------

def invoice(request,pk):
    if request.user.is_authenticated:
        order = Order.objects.get(pk=pk)
        return render(request,'payments/invoice.html',{'order':order})

    else:
        return redirect('login')



def process_payment(request):
    tp = 0
    host = request.get_host()
    if request.user.is_authenticated:
        cart = Cart.objects.all()
        cartlist = []
        for cartobject in cart:
            if str(cartobject.customer.name).strip() == str(request.user).strip():
                tp += cartobject.totalprice()
                cartlist.append(cartobject)

        for products in cart:
            paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': str(int(tp*0.013)),
            'item_name': "products",
            'invoice': 123456789,
            'currency_code': 'USD',
            'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
            'return_url': 'http://{}{}'.format(host,reverse('payment_done')),
            'cancel_return': 'http://{}{}'.format(host,reverse('payment_cancelled')),
            }
        form = PayPalPaymentsForm(initial=paypal_dict)
        return render(request, 'payments/paypal_form.html', {'form': form})
        
        
    else:
        return redirect('login')


@csrf_exempt
def payment_done(request):
    if request.user.is_authenticated:
        cart = Cart.objects.all()
        for cartobject in cart:
            if str(cartobject.customer.name).strip() == str(request.user).strip():
                b = Order(name=cartobject.product.name,product=cartobject.product,customer=cartobject.customer,totalprice=cartobject.totalprice(),count=cartobject.count,payment_status = True, status ='Pending')
                b.save()
                Cart.delete(cartobject)
        return redirect('orders')
    
    else:
        return redirect('login')



@csrf_exempt
def payment_canceled(request):
    if request.user.is_authenticated:
        cart = Cart.objects.all()
        for cartobject in cart:
            if str(cartobject.customer.name).strip() == str(request.user).strip():
                b = Order(name=cartobject.product.name,product=cartobject.product,customer=cartobject.customer,totalprice=cartobject.totalprice(),count=cartobject.count,payment_status = False, status ='Pending')
                b.save()
                Cart.delete(cartobject)
        return redirect('orders')
    
    else:
        return redirect('login')



# ACCOUNTS-----------------------------------------------------------------------------------------------------------------------------------

def profile(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(name=str(request.user))
        context = {'customer':customer}
        return render(request,'ecom/profile.html',context)

    else:
        return redirect('login')

def editprofile(request):
    if request.user.is_authenticated:
        customer = get_object_or_404(Customer, name=request.user)
        if request.method == "POST":
            form = CustomerForm(data=request.POST,files=request.FILES,instance=customer)
            if form.is_valid():
                customer = form.save(commit=False)
                customer.date_created = timezone.now()
                customer.save()
                return redirect('profile')
        else:
            form = CustomerForm(instance=customer)
        return render(request, 'ecom/customerform.html', {'form': form})


    else:
        return redirect('login')


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'todolist/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                customer = Customer(name = str(request.user))
                customer.save()
                return redirect('home')
        else:
            return render (request,'accounts/signup.html', {'error':'Password does not match!'})
    else:
        return render (request,'accounts/signup.html')
        
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render (request,'accounts/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render (request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')

    
def changepassword(request):
    if request.method == "POST":
        if request.POST['passwordnew1'] == request.POST['passwordnew2']:
            user = auth.authenticate(username=request.user, password = request.POST['passwordold'])
            if user is not None:
                user = User.objects.get(username=str(request.user))
                user.set_password(str(request.POST['passwordnew1']))
                user.save()
                return redirect('login')

            else:
                return render (request,'accounts/resetpassword.html', {'error':'Oldpassword is incorrect!'})
        else:
            return render (request,'accounts/resetpassword.html', {'error':'Password does not match!'})
    else:
        return render (request,'accounts/resetpassword.html')



