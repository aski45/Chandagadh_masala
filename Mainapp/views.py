from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


from .models import Product,Member

# Create your views here.


def get_base_context() :
    products = Product.objects.filter()
    members = Member.objects.filter()
    context = {"products" : products, 'members':members}
    return context

def home(request) : 
    return render(request,'home.html',get_base_context())