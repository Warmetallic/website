from django.shortcuts import render, redirect
from .models import Image


# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {'images': images})

def projects(request):
    return render(request, 'projects.html', {})
