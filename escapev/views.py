from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from .models import InputForm
from escapev.compute import compute
import os

def index(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute(float(form2.m)*form2.Munit, float(form2.r)*form2.Runit)
            
    else:
        form = InputForm()
    context = {'form': form,
             'result': result,
             }
    return render(request, 'hw8.html', context)

    