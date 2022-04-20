#Django
from django.urls import path
#Views
from .views import *

urlpatterns = [
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact, name='contact'),
]
