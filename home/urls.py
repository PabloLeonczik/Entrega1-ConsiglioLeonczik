from home import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('personas-casamiento/', views.personas_casamiento, name = 'personas_casamiento'),
    path('crear-persona/', views.crear_persona, name='crear_persona'),
    path('about/', views.about, name='about'),
    
]

