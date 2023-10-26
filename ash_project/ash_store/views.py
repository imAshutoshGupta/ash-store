from django.shortcuts import render, HttpResponse, redirect
from product_app.models import Product
from ash_store.models import Cart
from django.db.models import Q

# Create your views here.
'''
views provide response to client by using:
1) HttpResponse()
2) render() - This function sends html file as response to browser.
Syntax - render(request,'filename.html',data)

'''


def homepage(request):

    # return HttpResponse('Hello from Home Page')
    context = {}
    context['msg'] = "hello all,, good morning!!!"
    context['x'] = 100
    context['y'] = 1000
    context['data'] = [10, 20, 30, 40, 50, 60]
    return render(request, 'ashstore/home.html', context)


def about(request):

    return HttpResponse('Hi this is about me')


def contact(request):

    return HttpResponse('This is my contact information')


def edit(request, id):
    print("ID to be edited:", id)
    return HttpResponse("ID to be updated:"+id)


def delete(request, id):
    print("ID to be deleted:", id)
    return HttpResponse("ID to be deleted:"+id)


def addition(request, x, y):
    res = int(x)+int(y)
    print("addition is:", res)
    return HttpResponse("Addition is:"+str(res))


def home(request):
    p = Product.objects.filter(is_available=True)
    context = {'pdata': p}
    return render(request, 'ashstore/index.html', context)


def cat_filter(request, cid):
    q1 = Q(cat=cid)
    q2 = Q(is_available=True)
    p = Product.objects.filter(q1 & q2)
   # p = Product.objects.filter(cat=cid)
    context = {'pdata': p}

    return render(request, 'ashstore/index.html', context)

def pricerange(request):

    min = request.GET['min']
    max = request.GET['max']

    if not min.isdigit() or not max.isdigit():
        context = {'errmsg' : "Enter a valid amount"}
        return render(request, 'ashstore/index.html', context)
    if int(min)<0 or int(max)<0:
        context = {'errmsg' : "Price cannot be negative"}
        return render(request, 'ashstore/index.html', context)
    elif int(min)>int(max):
        context = {'errmsg' : "Minimum price cannot be greater than maximum amount"}
        return render(request, 'ashstore/index.html', context)
    else:
        min=int(min)
        max=int(max)
        q1 = Q(price__gte=min)
        q2 = Q(price__lte=max)
        q3 = Q(is_available=True)
        p = Product.objects.filter(q1 & q2 & q3)
        context = {'pdata' : p}
        return render(request, 'ashstore/index.html', context)
    
def sort(request):
    spara = request.GET['q']

    if spara == 'asc':
        #p=Product.objects.order_by('price').filter(is_available=True)
        x='price'
    else:
        #p=Product.objects.order_by('price').filter(is_available=True)
        x='-price'
    
    p=Product.objects.order_by(x).filter(is_available=True)
    context = {'pdata' : p}
    return render(request, 'ashstore/index.html', context)

def search(request):
    x = request.GET['search']

    q1 = Q(name__icontains=x)
    q2 = Q(pdetails__icontains=x)
    p = Product.objects.filter(q1 | q2)
    context = {'pdata' : p}
    return render(request, 'ashstore/index.html', context)


def pdetails(request,pid):
    p = Product.objects.get(id=pid)
    context = { 'product' : p }
    return render(request, 'ashstore/product_details.html', context)


def about_us(request):
    return render(request, 'ashstore/about.html')


def contact_us(request):
    return render(request, 'ashstore/contact.html')


def cart(request):
    if request.user.is_authenticated:       #returns value as true or false depending upon the user is authenticated or not
        return render(request, 'ashstore/cart.html')
    else:
        return redirect('accounts/login')
    
def placeorder(request):
    if request.user.is_authenticated:
        return render(request, 'ashstore/placeorder.html')
    else:
        return redirect('accounts/login')
    
def add_to_cart(request,prod_id):
    if request.user.is_authenticated:

        user_id=request.user.id
        p_obj=Product.objects.get(id=prod_id)
        c=Cart.objects.create(uid=request.user,pid=p_obj)
        c.save()
        return HttpResponse("test")
    else:
        return redirect('/accounts/login')