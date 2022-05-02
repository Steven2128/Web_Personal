# Django
from django.urls import path
# Views
from .views import *

urlpatterns = [
    path('portfolio/', portfolio, name='portfolio'),
]