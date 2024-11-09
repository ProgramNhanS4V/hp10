from django.contrib.auth.models import User
from django.db import models
# from djangoProject.models import Product
# Create your models here.
 
class Product(models.Model):
    #id sẽ tự động được tạo, và tự đông set là primary key, primary key được dùng để tạo ra các mối quan hệ giữa các bảng, foreign key
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product', null=True, blank=True)
    description = models.TextField(max_length=1000, null=True)
    origin = models.CharField(max_length=100, default='')
    trademark = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=10, decimal_places=0)
    def getName(self):
        return self.name
    def getImage(self):
        return self.image
    def getDescription(self):
        return self.description
    def getPrice(self):
        return self.price
    def getOriginal(self):
        return self.origin
    def getTrademark(self):
        return self.trademark
 
class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='post', null=True, blank=True)
    def getTitle(self):
        return self.title
    def getDate(self):
        return self.date
    def getContent(self):
        return self.content
    def getDescription(self):
        return self.description
 
class Comment(models.Model):
    content = models.TextField()
    author = User
    img_author = models.ImageField(upload_to='post/image', null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)