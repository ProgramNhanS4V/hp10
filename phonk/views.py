from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.views.generic import ListView, DetailView
from django.contrib.auth import authenticate, login, logout
from .form import ProductForm

# Create your views here.

# def home(req):
#     product = Product.objects.all()
#     print(product)
#     return render(req, 'home.html', context={ 'product': product})
class HomeView(ListView):
    model =  Product
    template_name = 'home.html'
    context_object_name = 'products'
def signin(req):
    return render(req, 'signin.html')
def signup(req):
    return render(req, 'signup.html')

def detail(req, id):
    product = Product.objects.get(id = id)
    return render(req, 'product_detail.html', context={ 'product': product})
#Hàm tìm kiếm sản phẩm
def resultSearch(req):
    #kiểm tra nếu cái phương thức gửi lên là POST
    if req.method == "POST":
        #lấy ra giá trị mà ng dùng nhập vào từ ô input
        search = req.POST.get("search")
        #kiểm tra nếu như search rỗng thì sẽ đưa ng dùng về lại trang home
        if not search:
            return redirect("home")
        #trong trường hợp search có giá trị, thì sẽ dùng hàm filter để lọc ra những sản phẩm trùng với từ khóa mà ng dùng nhập giá trị vào.
        #sự khác nhau giữa exact và contains: exact phải nhập đầy đủ giá trị thì mới hiển thị được sản phẩm, còn contains chỉ cần nhập từ khóa là dc r
        rs = Product.objects.filter(name__exact = search)
        return render(req, 'search.html', context= { 'rs': rs})

def login_user(req):
    if req.method == "POST":
        username = req.POST.get("username")
        password = req.POST.get("password")
        user = authenticate(req, username = username, password = password)
        if user is not None:
            login(req, user)
            return redirect("home")
        else:
            return redirect('signin')
    else:
        return render(req, 'signin.html')

def logout_user(req):
    logout(req)
    return redirect("home")

def view_product(req):
    product = Product.objects.all()
    return render(req, 'view_product.html', context={ 'product': product })

# def addProduct(req):
#     form = ProductForm(req.POST, req.FILES)
#     if req.method == "POST":
#         if form.is_valid():
#             form.save()
#             return redirect("product")
#     else:
#         form = ProductForm()
#     return render(req, "add_product.html", context= { 'form': form})

def editProduct(req, pk):
    product = get_object_or_404(Product, id = pk)
    form = ProductForm(req.POST, req.FILES, instance=product or None)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("product")
    else:
        form = ProductForm(instance=product)
    return render(req, "edit_product.html", context= { 'form': form, 'product': product})

def deleteProduct(req, pk):
    product = get_object_or_404(Product, id = pk)
    product.delete()
    return redirect("product")