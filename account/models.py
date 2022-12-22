from django.db import models
from django.contrib.auth.models import User

class ExtensionUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    link_pag = models.CharField(max_length=100, null=True, blank=True)