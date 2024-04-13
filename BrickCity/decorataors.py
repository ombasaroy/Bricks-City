from django.http import HttpResponse
from django.shortcuts import redirect

# This logic prevents an authenticated user from seeing
# the login and register page


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('bricksadmin')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


# Before writing the decorator for user roles base permission
# always ensure that you have created groups and assigned user tol groups


# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):
#             return view_func(request, *args, **kwargs)
#         return wrapper_func
#     return decorator

