from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .form import BusquedaUss, FormBlock
from .models import Block

def primera_vista(request):
    return render(request,'index.html')

def una_vista(request):
    
    if request.method == 'POST':
        form =FormBlock(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_creaccion')
            if not fecha:
                fecha = datetime.now()
            
            block1 = Block(
                          titulo=data.get('titulo'),
                          contenido=data.get('contenido'),
                          fecha_creaccion=fecha
                          ) 
            
            block1.save()
            return redirect('datos_usuario')
            
        else:
            return render(request,'index2.html',{'form':form})
    
    
    form_block=FormBlock()  
    return render(request,'index2.html',{'form': form_block} )








def segunda_vista(request):
    return render(request,'mi_template.html')







def Datos_usuario(request):
    titulo_de_busqueda =request.GET.get('titulo')
    
    if titulo_de_busqueda:
        datos_usuario = Block.objects.filter(titulo__icontains=titulo_de_busqueda)
    else:
        datos_usuario=Block.objects.all()
    
    form =BusquedaUss()
    return render(request,'datos_usuario.html',{'datos_usuario':datos_usuario,'form':form})