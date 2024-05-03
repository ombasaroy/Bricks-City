# This is where we customise our custom forms


from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PartnershipMessage, Test, MyPost, Advert


# Create our form below
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class SendPartnersMessage(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fullname'].label = 'Enter full name'
        self.fields['fullname'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': '',
            'type': 'text',
            'placeholder': 'Enter name',
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': '',
            'type': 'text',
            'placeholder': 'Enter your email here',
        })
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': '',
            'type': 'text',
            'placeholder': 'Enter subject here',
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': '',
            'type': 'text',
            'placeholder': 'Type your message here'
        })

    class Meta:
        model = PartnershipMessage
        fields = '__all__'


class CreateTestForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'


class MyPostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': True,
            'type': 'text',
            'placeholder': 'Enter post title'
        })
        self.fields['intro'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': True,
            'type': 'text',
            'placeholder': 'Enter post introduction',
        })
        self.fields['body'].widget.attrs.update({
            # 'class': 'form-control mb-3',
            'required': True,
            'type': 'textarea',
            'placeholder': 'Enter post body',
        })

        self.fields['author'].label = 'Admin is the default'
        self.fields['author'].widget.attrs.update({
            'class': 'form-control mb-3 width-100',
            'type': 'text',
            'disabled': True,
        })

        self.fields['featured_image'].label = 'Upload featured image'
        self.fields['featured_image'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': True,
            'type': 'image',
            'accept': 'image/*',
        })

    class Meta:
        model = MyPost
        fields = '__all__'


class AdvertForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['message'].label = ''
        self.fields['message'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': True,
            'type': 'text',
            'placeholder': 'Enter your advert'
        })
        self.fields['title'].label = ''
        self.fields['title'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': True,
            'type': 'text',
            'placeholder': 'Enter your title'
        })
        self.fields['image'].label = ''
        self.fields['image'].widget.attrs.update({
            'class': 'form-control mb-3',
            'required': True,
            'type': 'file',
            'accept': 'image/*'
        })

    class Meta:
        model = Advert
        fields = '__all__'
