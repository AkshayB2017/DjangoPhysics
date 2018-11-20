from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from .models import InputForm
from calculate.compute import compute
import os

def index(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            result = compute(float(form2.u) *form2.Uunit, float(form2.t)*form2.Tunit, float(form2.a)*form2.Aunit)
            form3=(form2.Uunit,form2.Tunit,form2.Aunit)   
    else:
        form = InputForm()
    context = {'form': form,
             'result': result,
             }
    return render(request, 'hw1.html', context)

    