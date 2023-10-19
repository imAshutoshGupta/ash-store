from django.shortcuts import render,HttpResponse
from product_app.models import Product

# Create your views here.
'''
views provide response to client by using:
1) HttpResponse()
2) render() - This function sends html file as response to browser.
Syntax - render(request,'filename.html',data)

'''

def homepage(request):

    #return HttpResponse('Hello from Home Page')
    context={}
    context['msg']="hello all,, good morning!!!"
    context['x']=100
    context['y']=1000
    context['data']=[10,20,30,40,50,60]
    return render(request,'ashstore/home.html',context)
def about(request):

    return HttpResponse('Hi this is about me')
def contact(request):

    return HttpResponse('This is my contact information')
def edit(request,id):
    print("ID to be edited:",id)
    return HttpResponse("ID to be updated:"+id)
def delete(request,id):
    print("ID to be deleted:",id)
    return HttpResponse("ID to be deleted:"+id)
def addition(request,x,y):
    res=int(x)+int(y)
    print("addition is:",res)
    return HttpResponse("Addition is:"+str(res))


def home(request):
    p = Product.objects.filter(is_available = True)
    context = {'pdata' : p}
    return render(request, 'ashstore/index.html', context)

def pdetails(request):
    return render(request, 'ashstore/product_details.html')

def cat_filter(request,cid):
    p = Product.objects.filter(cat=cid)
    context = {'pdata' : p}

    return render(request, 'ashstore/index.html', context)


def about_us(request):
    return render(request, 'ashstore/about.html')

def contact_us(request):
    return render(request, 'ashstore/contact.html')

def cart(request):
    return render(request, 'ashstore/cart.html')

