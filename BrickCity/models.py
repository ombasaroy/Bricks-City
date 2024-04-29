from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here
class PartnershipMessage(models.Model):
    fullname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = RichTextField(max_length=100, blank=True, null=True)

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
    intro = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextField(max_length=3000, blank=True, null=True)
    author = models.CharField(default='Admin', max_length=20, blank=True, null=True)
    featured_image = models.ImageField(upload_to='posts/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Advert(models.Model):
    message = models.CharField(max_length=500, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.message
