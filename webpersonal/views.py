# Django
from django.shortcuts import render, HttpResponse


def home(request):
    """Vista de inicio"""
    return render(request, 'core/home.html')


def about(request):
    """Vista sobre mi"""
    return render(request, 'core/about.html')


def contact(request):
    """Vista contacto"""
    return render(request, 'core/contact.html')