from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView

def index(request):
    return render(request, 'index.html')
