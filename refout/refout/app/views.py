from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                

                #criação do profile

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model)
                new_profile.save()
                return redirect('signin')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')



            #criação do profile



    else:
        return render(request, 'signup.html') 

def signin(request):

    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invalid password or email')
    else:
        return render(request, 'signin.html')

def notifications(request):
    return render(request, 'notifications.html')

def profile(request):
    return render(request, 'profile.html')

def post(request):
    if request.method == 'POST':
        image = request.POST['image']
        referencia = request.POST['referencia']
        
    else:
        return render(request, 'post.html')