from django.contrib import admin
from . models import Message, Test, MyPost, Advert, BookSession


# Register your models here.
admin.site.register(Message)
admin.site.register(Test)
admin.site.register(MyPost)
admin.site.register(Advert)
admin.site.register(BookSession)
