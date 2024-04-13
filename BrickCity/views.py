from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post

# imports for logging in and loging out
from django.contrib.auth import authenticate, login, logout

# import for signing up
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, CreatePostForm

from .decorataors import unauthenticated_user


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

# @unauthenticated_user
# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('bricksadmin')
#     else:
#         form = CreateUserForm
#
#         if request.method == 'POST':
#             form = CreateUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = form.cleaned_data.get('username')
#                 messages.success(request, 'Account was created for ' + user)
#                 return redirect('signin')
#
#         context = {'form': form}
#         return render(request, 'signup.html', context)

@unauthenticated_user
def signup(request):
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


@unauthenticated_user
def signin(request):
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
    posts = Post.objects.all()[:4]

    context = {"nav": 'index', 'posts': posts}
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
    posts = Post.objects.all()

    context = {'nav': 'blog', 'posts': posts}
    return render(request, 'bricks/blog.html', context)


def single_blog(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post}
    return render(request, 'bricks/single-blog.html', context)


# ADMIN STARTS HERE
# @login_required(login_url='signin')
# def bricksadmin(request):
#     return render(request, 'bricksadmin/home.html')
# ADMIN ENDS HERE


#     Admin starts here
@login_required(login_url='signin')
def bricksadmin(request):

    posts = Post.objects.all()
    posts_count = Post.objects.all().count()
    context = {'posts': posts, 'posts_count': posts_count}
    return render(request, 'bricksadmin/home.html', context)


#     Admin ends here


def createpost(request):
    if request.method == 'POST':
        title = request.POST.get('title').title()
        snippet = request.POST.get('snippet')
        body = request.POST.get('body')
        featured_image = request.FILES.get('featured')
        thumbnail = request.FILES.get('thumbnail')

        query = Post(title=title, snippet=snippet, body=body, featured_image=featured_image, thumbnail=thumbnail)
        query.save()
        messages.success(request, title + " created successfully")
        return redirect('bricksadmin')

    return render(request, 'bricksadmin/createpost.html')





def editpost(request):
    return render(request, 'bricksadmin/editpost.html')


def comments(request):
    return render(request, 'bricksadmin/comments.html')


def stats(request):
    posts_count = Post.objects.all().count()
    context = {'posts_count': posts_count}
    return render(request, 'bricksadmin/stats.html', context)
