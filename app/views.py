from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *

def student(request):
    SO=StudentForm()
    d={'so':SO}

    if request.method=='POST':
        sfo=StudentForm(request.POST)
        if sfo.is_valid():
            #return HttpResponse(str(sfo.cleaned_data))
            return HttpResponse('data is submitted successfully')
        else:
            return HttpResponse('Invalid data')

    return render(request,'student.html',d)