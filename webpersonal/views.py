#Django
from django.shortcuts import render, HttpResponse


def home(request):
    """Vista de inicio"""
    return render(request, 'home.html')


def about(request):
    """Vista sobre mi"""
    return render(request, 'about.html')


def contact(request):
    """Vista contacto"""
    return render(request, 'contact.html')