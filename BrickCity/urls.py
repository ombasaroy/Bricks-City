from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('partnerships/', views.partnerships, name='partnerships'),
    path('blog/', views.blog, name='blog'),
    path('single-blog/', views.single_blog, name='single_blog'),
    path('bricksadmin/', views.bricksadmin, name='bricksadmin'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminsignup/', views.adminsignup, name='adminsignup'),

]
