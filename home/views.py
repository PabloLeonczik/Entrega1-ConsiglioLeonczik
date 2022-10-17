from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render,redirect
import random
from home.forms import PersonaFormulario, BusquedaPersonaFormulario

from home.models import Persona

def crear_persona(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        persona = Persona(nombre=nombre, apellido=apellido, edad=random.randrange(1,99), fecha_nacimiento=datetime.now())
        persona.save()
        return redirect('personas_casamiento')

    formulario = PersonaFormulario
    return render(request, 'crear_persona.html', {'formulario':formulario})
    
def personas_casamiento(request):
    nombre = request.GET.get('nombre', None)
    if nombre:
        personas = Persona.objects.filter(nombre__icontains=nombre)
    else:
        personas = Persona.objects.all()
    
    formulario = BusquedaPersonaFormulario()
    return render(request, 'ver_personas.html', {'personas': personas, 'formulario':formulario})

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')