from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

#authenticate(): this function verifies the username and password with all the records in auth_user table in database.
#if username and password are correct this function returns the object or row from the database table auth_user otherwise it returns None

# Create your views here.
def homepage(request):
    return HttpResponse("Hi from accounts page")

def user_login(request):
    if request.method=="GET":
        return render(request,'accounts/login.html')
    else:
        iname=request.POST['iname']
        ipass=request.POST['ipass']

        #validation
        if iname=='' or ipass=='':
            context={'errmsg':"Username/Email and Password cannot be blank"}
            return render(request,'accounts/login.html',context)
        #elif iname!=username or 
        else:
            u=authenticate(username=iname,password=ipass)

            if u is not None:
                login(request,u)    #It starts session and stores objects of authenticated users in sessions.
                return redirect('/')
            else:
                context={'errmsg':"invalid username or password"}

                return render(request, 'accounts/login.html',context)

def user_register(request):
    if request.method=="GET":
        return render(request,'accounts/register.html')
    else:
        uname=request.POST['iname']
        uemail=request.POST['iemail']
        upass=request.POST['ipass']
        ucpass=request.POST['cipass']
        
        if uname=='' or uemail=='' or upass=='' or ucpass=='':
            context = {'errmsg': "Fields cannot be empty"}
            return render(request,'accounts/register.html',context)
        elif len(upass)<8:
            context = {'errmsg': "Password must be minimum 8 characters in length"}
            return render(request,'accounts/register.html',context)
        elif upass.isdigit():
            context = {'errmsg': "Password cannot be entirely in digits"}
            return render(request,'accounts/register.html',context)
        elif upass!=ucpass:
            context = {'errmsg': "Password mismatch"}
            return render(request,'accounts/register.html',context)
        else:
            u = User.objects.create(username=uname,email=uemail,password=upass)
            u.set_password(upass)
            u.save()
            context = {'success' : "User created successfully"}
            return render(request,'accounts/register.html',context)
        
def user_logout(request):
    logout(request)
    return redirect('/')