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
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            print('*******************')
            print('I am logged in')
            print('*******************')
            return redirect('homepage')
        else:
            print("*************")
            print("I am somewhere else")
            print("*************")
            return render(request,'accounts/login.html',{'error':'wrong pass or username'})

    return render(request,'accounts/login.html',{})



def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('homepage')
