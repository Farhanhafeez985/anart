from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from Backend.models import *


# Create your views here.
def home(request):
    data = {"1": 1, "2": 2}
    context = {'data': data}
    return render(request, 'index.html', context)


def contact(request):
    data = {"1": 1, "2": 2}
    context = {'data': data}
    return render(request, 'contact.html', context)


def project(request):
    data = {"1": 1, "2": 2}
    context = {'data': data}
    return render(request, 'project.html', context)


def about(request):
    data = {"1": 1, "2": 2}
    context = {'data': data}
    return render(request, 'about.html', context)


def gallery(request):
    data = {"1": 1, "2": 2}
    context = {'data': data}
    return render(request, 'ImageGallery.html', context)


def blogs(request):
    data = {"1": 1, "2": 2}
    context = {'data': data}
    return render(request, 'blogs.html', context)


def Signup(request):
    if request.method == 'POST' and request.FILES:
        postData = request.POST
        firstName = postData.get('fname')
        lastName = postData.get('lname')
        username = postData.get('uname')
        email = postData.get('email')
        password = postData.get('password')
        pic = request.FILES['image']
        data = User.objects.create(FirstName=firstName, LastName=lastName, UserName=username, Email=email,
                                   Password=password, ProfilePic=pic)
        data.save()
        messages.success(request, 'Registration completed')
        return redirect('signup')
    return render(request, 'UserForms.html')
