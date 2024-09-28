from django.shortcuts import render
from .models import Product

# Create your views here.

def home(req):
    product = Product.objects.all()
    print(product)
    return render(req, 'home.html', context={ 'product': product})
def signin(req):
    return render(req, 'signin.html')
def signup(req):
    return render(req, 'signup.html')

def detail(req, id):
    product = Product.objects.get(id = id)
    return render(req, 'product_detail.html', context={ 'product': product})