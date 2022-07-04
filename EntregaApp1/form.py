from django import forms

class FormBlock(forms.Form):
    titulo=forms.CharField(max_length=30)
    contenido=forms.CharField(max_length=120)
    fecha_creaccion=forms.DateField(required=False)
    
class BusquedaUss(forms.Form):
    titulo=forms.CharField(max_length=30 , required=False)    