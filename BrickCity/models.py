from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    snippet = models.CharField(max_length=200, blank=True, null=True)
    body = models.CharField(max_length=200)
    author = models.CharField(max_length=50, default='Admin', blank=True, null=True)
    featured_image = models.ImageField(upload_to='blog', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='blog', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
