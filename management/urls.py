from django.urls import path
from . import views
urlpatterns = [
    path('add', views.add_product, name = "add"),
    path('edit', views.edit_product, name = "edit"),
    path('view', views.view_product, name = "view"),
]
