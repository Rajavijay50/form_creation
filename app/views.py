from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
# Create your views here.

def djforms(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        
        if SFDO.is_valid():
        

            # return HttpResponse(str(SFDO.cleaned_data))
            # return HttpResponse(SFDO.cleaned_data['Sname'])

            return HttpResponse(SFDO.cleaned_data)

    return render(request,'djforms.html',d)
