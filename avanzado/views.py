from django.shortcuts import render, redirect
from avanzado.models import Mascota
from avanzado.forms import MascotaFormulario


from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin

def ver_mascotas(request):
    
    mascota = Mascota.objects.all()
    
    return render(request,'ver_mascotas.html', {'mascotas':mascota})

@login_required(login_url= '/account/login')
def crear_mascotas(request):
    
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            mascota = Mascota(nombre=datos['nombre'], 
                    tipo= datos['tipo'], 
                    edad=datos['edad'], 
                    fecha_nacimiento=datos['fecha_nacimiento'],
                    descripcion=datos['descripcion'],
                    )
            mascota.save()
            return redirect('ver_mascotas')
        else:
            return render(request, 'crear_mascota.html', {"formulario" : formulario})
    
    formulario = MascotaFormulario()
    
    return render(request, 'crear_mascota.html', {"formulario" : formulario})

def editar_mascota(request, id):
      
    mascota = Mascota.objects.get(id=id)
      
    if request.method == 'POST':
        formulario = MascotaFormulario(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            mascota.nombre = datos['nombre']
            mascota.tipo = datos['tipo']
            mascota.edad = datos['edad']
            mascota.fecha_nacimiento = datos['fecha_nacimiento']
            mascota.descripcion = datos['descripcion']
            
            mascota.save()
            return redirect('ver_mascotas')
    
    formulario = MascotaFormulario(
        initial={
            'nombre':mascota.nombre,
            'tipo':mascota.tipo,
            'edad':mascota.edad,
            'fecha_nacimiento':mascota.fecha_nacimiento,
            'descripcion':mascota.descripcion
        }
        )
    
    return render(request, 'editar_mascota.html', {"formulario" : formulario, 'mascota' : mascota})

def eliminar_mascota(request, id):
    mascota = Mascota.objects.get(id=id)
    mascota.delete()
    return redirect('ver_mascotas')


class ListaMascotas(ListView):
    model= Mascota
    template_name = 'ver_mascotas_cbv.html'
    
class CrearMascota(CreateView):
    model = Mascota
    success_url = '/avanzado/mascotas/'
    template_name = 'crear_mascota_cbv.html'
    fields = ['nombre', 'tipo', 'edad', 'fecha_nacimiento', 'descripcion']

class EditarMascota(UpdateView):
    model = Mascota
    success_url = '/avanzado/mascotas/'
    template_name = 'editar_mascota_cbv.html'
    fields = ['nombre', 'tipo', 'edad', 'fecha_nacimiento', 'descripcion']
    
class EliminarMascota(DeleteView):
    model = Mascota
    success_url = '/avanzado/mascotas/'
    template_name = 'eliminar_mascota_cbv.html'