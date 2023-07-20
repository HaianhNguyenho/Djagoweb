from django.shortcuts import render,redirect
import json
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def detail(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_id':0, 'get_total':0}
    id = request.GET.get('id','')
    products = Product.objects.filter(id=id)
    context={'items':items,'order':order,'products':products}
    return render(request, 'app/detail.html',context)


def contact(request):
    context = {}
    return render(request, 'app/contact.html', context)

def search(request):
    if request.method =="POST":
        searched = request.POST["searched"]
        values = Product.objects.filter(name__contains = searched)
    return render(request, 'app/search.html',{"searched":searched,"values":values})

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:login')
    context = {'form':form}
    return render(request,'app/register.html',context)

def loginPage(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app:home')
        else:
            messages.info(request, 'Username và mật khẩu không đúng!')
        if request.user.is_authenticated:
            return redirect('app:home')
    context = {}
    return render(request, 'app/login.html', context)
def logoutPage(request):
    logout(request)
    return redirect('app:login')

def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order,create = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else: 
        items=[]
        order={'get_id':0,'order':0}
    products = Product.objects.all()
    context={'products':products}
    return render(request, 'app/home.html',context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_id':0, 'get_total':0}
    context={'items':items,'order':order}
    return render(request, 'app/cart.html',context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []

        order = {'get_id':0, 'get_total':0}

    context={'items':items,'order':order}

    return render(request, 'app/checkout.html',context)

def addgh(request):
    data = json.loads(request.body)
    productID = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id = productID)
    order, created = Order.objects.get_or_create(customer = customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product=product)
    if action == 'add':
        orderItem.quantity +=1
    elif action == "remove":
        orderItem.quantity -=1
    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()
        
    return JsonResponse('added', safe=False)