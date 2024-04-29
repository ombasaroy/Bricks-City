from django.contrib import admin
from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('partnerships/', views.partnerships, name='partnerships'),
    path('advert/', views.advert, name='advert'),
    path('blog/', views.blog, name='blog'),
    path('single-blog/<id>', views.single_blog, name='single_blog'),
    path('bricksadmin/', views.bricksadmin, name='bricksadmin'),

    path('createpost/', views.createpost, name='createpost'),
    path('editpost/<id>', views.editpost, name='editpost'),
    path('deletepost/<id>', views.deletepost, name='deletepost'),

    path('createadvert/', views.createadvert, name='createadvert'),
    path('editadvert/<id>', views.editadvert, name='editadvert'),


    path('messages/', views.mymessages, name='messages'),
    path('stats/', views.stats, name='stats'),
    path('test/', views.test, name='test'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),

]
