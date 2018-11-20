from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from .models import InputForm
from powerv.compute import compute
import os

def index(request):
    os.chdir(os.path.dirname(__file__))
    result = None
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form2 = form.save(commit=False)
            if form2.tunit == 0:
                result = compute(float(form2.a)*form2.aunit, float(form2.t), float(form2.d)*form2.dunit)
            elif form2.tunit == 1:
                result = compute(float(form2.a)*form2.aunit, float(form2.t) + float(273.15), float(form2.d)*form2.dunit)
            elif form2.tunit == 2:
                result = compute(float(form2.a)*form2.aunit, float(form2.t-32)*0.555556 + 273.15, float(form2.d)*form2.dunit)
            
    else:
        form = InputForm()
    context = {'form': form,
             'result': result,
             }
    return render(request, 'hw13.html', context)

    