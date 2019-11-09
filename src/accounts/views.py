from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html',{'error':'name already taken'})
            except User.DoesNotExist:
                user=User.objects.create_user(request.POST['username'],request.POST['password1'])
                auth.login(request,user)
                return redirect('homepage')


    else:
        return render(request,'accounts/signup.html', {'error': 'password dont match'})

    return render(request,'accounts/signup.html',{})



def login(request):
    return render(request,'accounts/login.html',{})



def logout(request):
    return render(request,'accounts/signup.html',{})