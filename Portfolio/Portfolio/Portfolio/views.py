from django.http import HttpResponse
from django.shortcuts import render

def Projects(request):
    return render(request, 'projects.html')

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')