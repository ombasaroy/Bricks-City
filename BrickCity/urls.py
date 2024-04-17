from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('partnerships/', views.partnerships, name='partnerships'),
    path('blog/', views.blog, name='blog'),
    path('single-blog/<id>', views.single_blog, name='single_blog'),
    path('bricksadmin/', views.bricksadmin, name='bricksadmin'),
    path('createpost/', views.createpost, name='createpost'),
    path('editpost/<id>', views.editpost, name='editpost'),
    path('messages/', views.mymessages, name='messages'),
    path('stats/', views.stats, name='stats'),
    path('test/', views.test, name='test'),


]
