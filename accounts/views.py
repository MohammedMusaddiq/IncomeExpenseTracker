from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from iet.models import UserBalance
from .models import User


def handelLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Logged in successfully as {email}')
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('iet:dashboard')
        else:
            messages.error(request, 'Invalid Credentials. Please Try Again With Correct Credentials')

    context = {
        'title': 'Login',
        'navbar': 'Login',

    }
    return render(request, 'accounts/login.html', context)


def handelSignup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        see_user = User.objects.filter(email=email)
        if User.objects.filter(email=email).exists():
            messages.error(request, 'User With Email Already Exists, Please Try Signing in')
        else:
            user = User.objects.create_user(email=email, name=username, password=password)
            user.save()
            messages.success(request, 'Registered Successfully, Login Now')
            user_balance_obj = UserBalance(
                user=user,
                balance_amount=0,
            )
            user_balance_obj.save()
            return redirect('accounts:login')
    context = {
        'title': 'Signup',
        'navbar': 'Sign up',
    }
    return render(request, 'accounts/signup.html', context)


def handelLogout(request):
    logout(request)
    messages.success(request, 'Logged out Successfully')
    return redirect('accounts:login')
