from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User

# Create your views here.
def index(request):
    return HttpResponse(render(request, 'index.html'))

def register_page(request):
    return HttpResponse(render(request, 'register_page.html'))

def register(request):
    name = request.POST['name']
    phone = request.POST['phone']
    password = request.POST['password']
    user = User(name=name, phone=phone, password=password)
    user.save()
  
    return HttpResponseRedirect(reverse('index'))


def login_page(request):   
    return HttpResponse(render(request, 'login_page.html'))


def user(request):
    phone = request.GET['phone']
    user = User.objects.get(phone=phone)
    context ={'user': user} 
    return HttpResponse(render(request, "user.html", context))
    