from django import forms
from ckeditor.widgets import CKEditorWidget


class MascotaFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    tipo = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    fecha_nacimiento = forms.DateField()
    descripcion = forms.CharField(widget=CKEditorWidget())