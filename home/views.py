from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

def index(request):
    return render(request, 'index.html')

def kinematics(request):
    return render(request, 'kinematics.html')

def dynamics(request):
    return render(request, 'dynamics.html')

def thermodynamics(request):
    return render(request, 'thermodynamics.html')

def electronics(request):
    return render(request, 'electronics.html')