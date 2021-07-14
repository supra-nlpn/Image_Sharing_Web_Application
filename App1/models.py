from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
# Create your models here.
class User(AbstractUser):
    userpic = models.ImageField(upload_to="profliepics/", default="def_1.jpg")

class Image(models.Model):
 photo = models.ImageField(upload_to="myimage/", default="def_1.jpg")
 caption = models.TextField(max_length=200)
 uid = models.ForeignKey(User, on_delete=models.CASCADE)
 date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    imageid = models.ForeignKey(Image, on_delete=models.CASCADE)
    uname = models.TextField(max_length=50, null= True)
    comment = models.TextField(max_length=200)