from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')  # use URL name instead of 'register/'
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already registered")
                return redirect('register')
            else:
                user_reg = User.objects.create_user(username=username, email=email, password=password)
                user_reg.save()
                messages.info(request, "Successfully created")
                return redirect('/')  # redirect to home or login
        else:
            messages.info(request, "Passwords do not match")
            return redirect('register')  # return to registration page
    return render(request, 'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('register/')
    return render(request,'log.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


