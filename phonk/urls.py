from django.urls import path
from . import views
from .views import HomeView
urlpatterns = [
    path('home', HomeView.as_view(), name = "home"),
    path('signin', views.login_user, name = "signin"),
    path('logout', views.logout_user, name = "logout"),
    path('search', views.resultSearch, name = "search"),
    path('signup', views.signup, name = "signup"),
    path('detail/<int:id>', views.detail, name = "detail"),
    path('product', views.view_product, name = "product"),
    path('product/edit/<int:pk>', views.editProduct, name = "edit-product"),
]