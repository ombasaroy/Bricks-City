from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here
class Message(models.Model):
    fullname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    message = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.fullname


class Test(models.Model):
    fullname = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='test/', blank=True, null=True)
    bio = RichTextField()
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.fullname


class MyPost(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    intro = models.CharField(max_length=1000, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    author = models.CharField(default='Admin', max_length=20, blank=True, null=True)
    featured_image = models.ImageField(upload_to='posts/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Advert(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    message = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='adverts/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title


class BookSession(models.Model):
    fullname = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    date_booked = models.DateField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname
