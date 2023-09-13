from django.shortcuts import render

# Create your views here.

def homepage(request):
    return HttpResponse('hello from homepage of product_app')