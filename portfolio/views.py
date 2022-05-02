# Django
from django.shortcuts import render
# Models
from .models import Project

def portfolio(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})
