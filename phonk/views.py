from django.shortcuts import render
from .models import Product

# Create your views here.

def home(req):
    product = Product.objects.all()
    return render(req, 'home.html', context={ 'product': product})
def signin(req):
    return render(req, 'signin.html')
def signup(req):
    return render(req, 'signup.html')