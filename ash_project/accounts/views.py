from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):
    return HttpResponse("Hi from accounts page")

def user_login(request):
    if request.method=="GET":
        return render(request,'accounts/login.html')
    else:
        iname=request.POST['iname']
        ipass=request.POST['ipass']

        if iname=='' or ipass=='':
            context={'errmsg':"Fields cannot be empty"}
            return render(request,'accounts/login.html',context)
        else:
            pass

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
