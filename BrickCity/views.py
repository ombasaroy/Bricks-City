from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# imports for logging in and loging out
from django.contrib.auth import authenticate, login, logout

# import for signing up
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm


# def signup(request):
#     form = UserCreationForm
#
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#
#     context = {'form': form}
#     return render(request, 'signup.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('bricksadmin')
    else:
        form = CreateUserForm

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('signin')

        context = {'form': form}
        return render(request, 'signup.html', context)
    return render(request, 'signup.html', context)


def signin(request):
    if request.user.is_authenticated:
        return redirect('bricksadmin')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('bricksadmin')
            else:
                messages.info(request, 'Username or password is incorrcet')
                return redirect('signin')
        else:
            return render(request, 'signin.html')


def logoutuser(request):
    logout(request)
    return redirect('signin')


def index(request):
    context = {"nav": 'index'}
    return render(request, 'bricks/index.html', context)


def services(request):
    context = {"nav": 'services'}
    return render(request, 'bricks/services.html', context)


def about(request):
    context = {"nav": 'about'}
    return render(request, 'bricks/about.html', context)


def contact(request):
    context = {"nav": 'contact'}
    return render(request, 'bricks/contact.html', context)


def partnerships(request):
    return render(request, 'bricks/partnerships.html')


def blog(request):
    context = {'nav': 'blog'}
    return render(request, 'bricks/blog.html', context)


def single_blog(request):
    return render(request, 'bricks/single-blog.html')


# ADMIN STARTS HERE
# @login_required(login_url='signin')
# def bricksadmin(request):
#     return render(request, 'bricksadmin/home.html')
    # ADMIN ENDS HERE


#     Admin starts here
@login_required(login_url='signin')
def bricksadmin(request):
    return render(request, 'bricksadmin/home.html')
#     Admin ends here


