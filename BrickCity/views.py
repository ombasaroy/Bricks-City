from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"nav": 'index'}
    return render(request, 'index.html', context)


def services(request):
    context = {"nav": 'services'}
    return render(request, 'services.html', context)


def about(request):
    context = {"nav": 'about'}
    return render(request, 'about.html', context)


def contact(request):
    context = {"nav": 'contact'}
    return render(request, 'contact.html', context)