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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': '',
            'type': 'text',
            'placeholder': 'Enter post title here',
        })
        self.fields['snippet'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': '',
            'type': 'text',
            'placeholder': 'Enter Snippet',
        })

        self.fields['intro'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': '',
            'type': 'text',
            'placeholder': 'Enter intro',
        })
        self.fields['body'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': '',
            'type': 'text',
            'placeholder': 'Enter your body here',
        })
        self.fields['featured_image'].label = 'Featured Image'
        self.fields['featured_image'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': '',
            'type': 'image',
            'accept': 'image/*'
        })
        self.fields['thumbnail'].label = 'Thumbnail'
        self.fields['thumbnail'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': '',
            'type': 'image',
            'accept': 'image/*'

        })
        self.fields['author'].label = 'Created by'
        self.fields['author'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': '',
            'type': 'text',
            'disabled': True

        })

        self.fields['quote'].widget.attrs.update({
            'class': 'form-control mb-3',
            'type': 'text',
            'placeholder': 'Enter quote',
        })

    class Meta:
        model = Post
        fields = '__all__'

