from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    snippet = models.CharField(max_length=200,blank=True, null=True)
    intro = models.CharField(max_length=300, blank=True, null=True)
    body = RichTextField()
    quote = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=50, default='Admin')
    featured_image = models.ImageField(upload_to='blog', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='blog', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
