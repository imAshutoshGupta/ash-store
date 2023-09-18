from django.shortcuts import render,HttpResponse

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
        is_avail=request.POST['cat']

        print("Product Name:",name)
        print("Product Amount:",amt)
        print("Quantity:",qty)
        print("Category:",cat)
        print("Availability:",is_avail)
        return HttpResponse("In data fetched")
    
