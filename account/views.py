from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login
from account.forms import MiFormularioDeCreacion, EditarPerfilFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from account.models import ExtensionUsuario

def mi_login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()
            login(request,usuario)
            extensionUsuario, esNuevo = ExtensionUsuario.objects.get_or_create(user=request.user)
            return redirect('index')
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'account/login.html', {'formulario': formulario})

def about(request):
    return render(request, 'about.html', {} )

def registrar(request):
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('index')

    else:
        formulario = MiFormularioDeCreacion()
        
    
    return render(request, 'account/registrar.html', {'formulario': formulario})

@login_required
def perfil(request):
    
    return render(request, 'account/perfil.html', {} )

@login_required
def editar_perfil(request):
    user = request.user

    if request.method == 'POST':
        formulario = EditarPerfilFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            if info_nueva.get('first_name'):
                user.first_name = info_nueva.get('first_name')
            if info_nueva.get('last_name'):
                user.last_name = info_nueva.get('last_name')
            user.email = info_nueva.get('email') if info_nueva.get('email') else user.email
            user.extensionusuario.avatar = info_nueva['avatar']
            user.extensionusuario.descripcion = info_nueva['descripcion']
            user.extensionusuario.link_pag = info_nueva['link_pag']

            user.extensionusuario.save()
            request.user.save()

            return redirect('perfil')

    else:
        formulario = EditarPerfilFormulario(initial={
            'first_name': request.user.first_name, 
            'last_name': request.user.last_name, 
            'email': request.user.email,
            'descripcion': user.extensionusuario.descripcion,
            'link_pag': user.extensionusuario.link_pag,
            'avatar': user.extensionusuario.avatar,})

    return render(request, 'account/editar_perfil.html', {'formulario': formulario} )

class CambiarContra(LoginRequiredMixin, PasswordChangeView):
    template_name = 'account/cambiar_contra.html'
    success_url = '/account/perfil'
   