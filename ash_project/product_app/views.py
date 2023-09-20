from django.shortcuts import render,HttpResponse,redirect
from . import models
from product_app.models import Product

# Create your views here.
def homepage(request):

    return HttpResponse('Hello from Homepage of Productapp')

def add_product(request):
    print("Method Name:",request.method)
    if request.method=="GET":
       print("In if GET section")
       return render(request,'product_app/product_app.html')
    else:
        print("In else POST section")
        name=request.POST['pname']
        amt=request.POST['price']
        qty=request.POST['qty']
        cat=request.POST['cat']
        is_avail=request.POST['is_avail']

        print("Product Name:",name)
        print("Product Amount:",amt)
        print("Quantity:",qty)
        print("Category:",cat)
        print("Availability:",is_avail)
        
    
    #validations
    #insert record into table
        p = Product.objects.create(name=name,price=amt,qty=qty,cat=cat,is_available=is_avail)
        print(p)
        p.save()
        # return HttpResponse("data inserted")
        return redirect('/product_app/productdash')
    
def product_dashboard(request):
    #fetch data from model or table
    p= Product.objects.all() #select * from product_app_product
    context={}
    '''
    print(p)
    print(p[0])
    print(p[1])
    print("Product Name:",p[0].name)
    print("Product Name:",p[0].price)
    print("Product Name:",p[1].name)
    print("Product Name:",p[1].price)
    print("Using Loop:")
    for x in p:
        print(x)
        print(x.name)
        print(x.price)
        print(x.is_available)
    '''
    context['products']=p  #using dictionary keys to access html values
    return render(request,'product_app/dashboard.html',context)
