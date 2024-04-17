from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# import for sending emails
from django.core.mail import send_mail

from .models import MyPost

# imports for logging in and loging out
from django.contrib.auth import authenticate, login, logout

# import for signing up
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, SendPartnersMessage, CreateTestForm, MyPostForm

from .decorataors import unauthenticated_user

# Importing custom forms


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

    posts = MyPost.objects.order_by('-date_created')[:4]

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
    form = SendPartnersMessage
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        message = request.POST.get('message')
        sender_email = request.POST.get('email')

        recipient_email = 'ombasaroy@gmail.com'  # Replace with your Gmail address

        send_mail(
            'Message from ' + fullname,
            message,
            sender_email,
            [recipient_email]
        )
        return HttpResponse('email_sent.html')

    context = {'form': form}
    return render(request, 'bricks/partnerships.html', context)


def blog(request):
    posts = MyPost.objects.all()

    context = {'nav': 'blog', 'posts': posts}
    return render(request, 'bricks/blog.html', context)


def single_blog(request, id):
    post = MyPost.objects.get(id=id)

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
    posts_count = MyPost.objects.all().count()
    posts = MyPost.objects.all()

    context = {'posts_count': posts_count, 'posts': posts}
    return render(request, 'bricksadmin/home.html', context)


#     Admin ends here


# def createpost(request):
#     if request.method == 'POST':
#         title = request.POST.get('title').title()
#         snippet = request.POST.get('snippet')
#         intro = request.POST.get('intro')
#         body = request.POST.get('body')
#         quote = request.POST.get('quote')
#         featured_image = request.FILES.get('featured')
#
#         query = Post(title=title, snippet=snippet, intro=intro, body=body, quote=quote, featured_image=featured_image)
#         query.save()
#         messages.success(request, title + " created successfully")
#         return redirect('bricksadmin')
#
#     return render(request, 'bricksadmin/createpost.html')

def createpost(request):
    form = MyPostForm

    if request.method == 'POST':
        form = MyPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Post was created successfully")
            return redirect('createpost')
        else:
            messages.error(request, 'FAILED!!')

    context = {'form': form}
    return render(request, 'bricksadmin/createpost.html', context)


def editpost(request, id):
    post = MyPost.objects.get(id=id)
    form = MyPostForm(instance=post)

    if request.method == 'POST':
        form = MyPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            messages.success(request, title + ' updated successfully')
            return redirect('bricksadmin')

    context = {'form': form, 'post': post}
    return render(request, 'bricksadmin/editpost.html', context)


def mymessages(request):
    return render(request, 'bricksadmin/messages.html')


def stats(request):
    posts_count = MyPost.objects.all().count()

    context = {'posts_count': posts_count}
    return render(request, 'bricksadmin/stats.html', context)


def test(request):
    form = CreateTestForm

    if request.method == "POST":
        form = CreateTestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'bricksadmin/test.html', context)



