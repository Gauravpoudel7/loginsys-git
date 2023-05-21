from django.contrib import messages
from telnetlib import LOGOUT
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login,logout

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1!=pass2:
            messages.error(request,"Password doesnot match")
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.error(request,"USERNAME TAKEN")
            return redirect('signup')
        else:
            myuser = User.objects.create_user(username=username , email=email,password=pass1)
            myuser.save()
            return redirect('login')

       

    return render(request,'signup.html')



def login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        logpass1 =request.POST.get('password')

        user = authenticate(request,username=uname,password=logpass1,)#using user models values
        if user is not None:
           auth_login(request,user)
           fname= user.get_username 
           return render(request,'home.html',{'fname':fname})
        else:
            return HttpResponse("username or password is incorrect")


       
            
    
    return render(request,'login.html')

def signout(request):
    logout(request)
    return redirect('login')
