from django.urls import path, include
from account import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.mi_login, name = 'login'),
    path('registrar/', views.registrar, name = 'registrar'),
    path('perfil/', views.perfil, name = 'perfil'),
    path('perfil/editar/', views.editar_perfil, name = 'editar_perfil'),
    path('perfil/cambiar_contra/', views.CambiarContra.as_view(), name = 'cambiar_contra'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name = 'logout'),
    path('about/', views.about, name='about'),
]