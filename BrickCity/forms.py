# This is where we customise our custom forms


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


# Create our form below
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'