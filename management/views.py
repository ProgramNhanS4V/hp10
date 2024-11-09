from django.shortcuts import render

# Create your views here.
def add_product(req):
    return render(req, 'product/add_product.html')
def edit_product(req):
    return render(req, 'product/edit_product.html')
def view_product(req):
    return render(req, 'product/view_product.html')
