from django.shortcuts import render
from .models import *
# Create your views here.
def mysite(request):
    
    return render(request, 'index.html')

def perfil(request):
    citas=Cita.objects.all()
    data={
        'citas': citas
    }
    return render(request, 'perfil.html', data)

