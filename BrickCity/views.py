from django.shortcuts import render

# Create your views here.


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
def bricksadmin(request):
    return render(request, 'bricksadmin/home.html')


def adminlogin(request):
    return render(request, 'bricksadmin/login.html')


def adminsignup(request):
    return render(request, 'bricksadmin/signup.html')


# ADMIN ENDS HERE

