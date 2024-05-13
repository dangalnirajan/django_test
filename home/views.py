from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):

    names = [
        {'name':'Suraj Kapali', 'age':23},
        {'name':'Suraj Acharya', 'age':35},
        {'name':'Samyog Paudel', 'age':20},
    ]
    return render(request, "index.html", context={'page':'Dashboard','names':names})

def contact(request):
    context = {'page':'Contact'}
    return render(request,"contact.html",context)

def about(request):
    context = {'page':'About'}
    return render(request,"about.html",context)