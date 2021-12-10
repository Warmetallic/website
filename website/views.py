from django.shortcuts import render, redirect
from .models import Image, Games, Certificate


# Create your views here.
def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {'images': images})

def projects(request):
    games = Games.objects.all()
    return render(request, 'projects.html', {'games': games})

def recommendations(request):
    certificates = Certificate.objects.all()
    return render(request, 'recommendations.html', {'certificates': certificates})
