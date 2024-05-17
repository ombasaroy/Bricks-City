from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# import for sending emails
from django.core.mail import send_mail

from .models import MyPost, Advert, BookSession, Message

# imports for logging in and loging out
from django.contrib.auth import authenticate, login, logout

# import for signing up
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, CreateTestForm, MyPostForm, AdvertForm, BookingForm, MessageForm

from .decorataors import unauthenticated_user

from django.core.paginator import Paginator

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
    return HttpResponse ('Access restricted')
    # form = CreateUserForm

    # if request.method == 'POST':
    #     form = CreateUserForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         user = form.cleaned_data.get('username')
    #         messages.success(request, 'Account was created for ' + user)
    #         return redirect('signin')

    # context = {'form': form}
    # return render(request, 'signup.html', context)


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
    myadverts = Advert.objects.all()

    context = {"nav": 'index', 'posts': posts, 'myadverts': myadverts}
    return render(request, 'bricks/index.html', context)


def services(request):
    context = {"nav": 'services'}
    return render(request, 'bricks/services.html', context)


def about(request):
    context = {"nav": 'about'}
    return render(request, 'bricks/about.html', context)


def contact(request):
    if request.method == 'POST':
        fullname = request.POST.get('name').title()
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(
                subject='MESSAGE',
                message=f'From: {email}\nName: {fullname}\nPhone Number: {phone}\nSubject: {subject}\nMessage: {message}',
                recipient_list=['brickscitylego.ke@gmail.com'],
                from_email= email,
                fail_silently=False,                
            )
        messages.success(request, 'Hi ' + fullname + '. Your message has been sent successfully')
        return redirect('contact')

    context = {"nav": 'contact'}
    return render(request, 'bricks/contact.html', context)
        


def partnerships(request):
    if request.method == 'POST':
        fullname = request.POST.get('name').title()
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(
                subject='PARTNERSHIP',
                message=f'From: {email}\nName: {fullname}\nPhone Number: {phone}\nSubject: {subject}\nMessage: {message}',
                recipient_list=['brickscitylego.ke@gmail.com'],
                from_email= email,
                fail_silently=False,                
            )
        messages.success(request, 'Hi ' + fullname + '. Your message has been sent successfully')
        return redirect('contact')

    context = {}
    return render(request, 'bricks/partnerships.html', context)


def blog(request):
    paginator = Paginator(MyPost.objects.all().order_by('-date_created'), 6)  # displays 4 products in a random order
    new_page = request.GET.get('page')
    posts = paginator.get_page(new_page)

    context = {'nav': 'blog', 'posts': posts}
    return render(request, 'bricks/blog.html', context)


def single_blog(request, id):
    post = MyPost.objects.get(id=id)

    context = {'post': post}
    return render(request, 'bricks/single-blog.html', context)


def booking(request):
    form = BookingForm

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('fullname')
            name = name.title()
            phone = form.cleaned_data.get('phone')
            email = form.cleaned_data.get('email')
            date = form.cleaned_data.get('date_booked')
            form.save()
            send_mail(
                subject='BOOKING',
                message=f'From: {email}\nName: {name}\nPhone Number: {phone}\nEmail: {email}\nDate Booked: {date}',
                recipient_list=['brickscitylego.ke@gmail.com'],
                from_email= email,
                fail_silently=False,                
            )
            send_mail(
                subject='LEGO BOOKING',
                message=f'Greetings {name}. Your have booked a Lego play date for {date}',
                recipient_list=[email],
                from_email= 'brickscitylego.ke@gmail.com',
                fail_silently=False,                
            )
            
            messages.success(request, 'Greetings ' + name + '. Your Booking is successful')
            return redirect('booking')
        else:
            name = form.cleaned_data.get('fullname')
            messages.success(request, 'Booking Failed')
            return redirect('booking')

    context = {'form': form}
    return render(request, 'bricks/booksession.html', context)


@login_required(login_url='signin')
def bookedsessions(request):
    bookings = BookSession.objects.order_by('date_booked')
    context = {'bookings': bookings}
    return render(request, 'bricksadmin/bookedsessions.html', context)


@login_required(login_url='signin')
def deletebooking(request, id):
    booking = BookSession.objects.get(id=id)

    if request.method == 'POST':
        booking.delete()
        fullname = booking.fullname
        messages.success(request, 'Booking for ' + fullname + ' deleted successfully')
        return redirect('bookedsessions')

    context = {'booking': booking}
    return render(request, 'bricksadmin/deletebooking.html', context)


#     Admin starts here
@login_required(login_url='signin')
def bricksadmin(request):
    paginator = Paginator(MyPost.objects.all().order_by('-date_created'), 10)  # displays 10 products begining with the most current
    new_page = request.GET.get('page')
    posts = paginator.get_page(new_page)
    
    posts_count = MyPost.objects.all().count()

    context = {'posts_count': posts_count, 'posts': posts}
    return render(request, 'bricksadmin/home.html', context)


@login_required(login_url='signin')
def createpost(request):
    form = MyPostForm

    if request.method == 'POST':
        form = MyPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            postname = form.cleaned_data.get('title')
            messages.success(request, postname + "Post was created successfully")
            return redirect('bricksadmin')
        else:
            messages.error(request, 'FAILED!!')

    context = {'form': form}
    return render(request, 'bricksadmin/createpost.html', context)


@login_required(login_url='signin')
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


@login_required(login_url='signin')
def deletepost(request, id):
    post = MyPost.objects.get(id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('bricksadmin')
    context = {'post': post}
    return render(request, 'bricksadmin/deletepost.html', context)


@login_required(login_url='signin')
def mymessages(request):
    posts_count = MyPost.objects.all().count()

    context = {'posts_count': posts_count}
    return render(request, 'bricksadmin/messages.html', context)


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


@login_required(login_url='signin')
def advert(request):
    myadverts = Advert.objects.order_by('-date_created')
    context = {'adverts': myadverts}
    return render(request, 'bricksadmin/adverts.html', context)


@login_required(login_url='signin')
def createadvert(request):
    form = AdvertForm

    if request.method == "POST":
        form = AdvertForm(request.POST, request.FILES)
        if form.is_valid():
            advert = form.cleaned_data.get('title')
            form.save()
            messages.success(request, advert + ' created successfully')
            return redirect('bricksadmin')
        else:
            form = AdvertForm

    context = {'form': form}
    return render(request, 'bricksadmin/createadvert.html', context)


@login_required(login_url='signin')
def editadvert(request, id):
    advert = Advert.objects.get(id=id)
    form = AdvertForm(instance=advert)

    if request.method == 'POST':
        form = AdvertForm(request.POST, request.FILES, instance=advert)
        if form.is_valid():
            form.save()
            advertname = form.cleaned_data.get('message')
            messages.success(request, advertname + ' updated successfully')
            return redirect('advert')
        else:
            form = AdvertForm(instance=advert)

    context = {'form': form}
    return render(request, 'bricksadmin/editadvert.html', context)


@login_required(login_url='signin')
def deleteadvert(request, id):
    ad = Advert.objects.get(id=id)

    if request.method == 'POST':
        ad.delete()
        return redirect('advert')
    context = {'ad': ad}
    return render(request, 'bricksadmin/deleteadvert.html', context)



