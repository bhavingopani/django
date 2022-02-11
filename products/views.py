from django.http import HttpResponse  #with this classs we can create an http response to return to the client or browser
from django.shortcuts import render
from .models import Product



#/products -> index  #this means we have map this url to this function
def index(request):#index is a main page of an app -- so we are naming it index
    products = Product.objects.all()   #to get all the products from our database
    # return HttpResponse('Hello World')  #creating an instance of this classs  and as angument to the constructor we pass HelloWorld
    return render(request, 'index.html', 
                  {'products': products})   #to render template


def newproducts(request):
    return HttpResponse('Please check all the products here')