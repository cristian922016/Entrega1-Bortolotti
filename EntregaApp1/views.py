from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

from .form import BusquedaUss, FormBlock
from .models import Block


def una_vista(request):
    
    if request.method == 'POST':
        form =FormBlock(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
            fecha = data.get('fecha_creaccion')
            if not fecha:
                fecha = datetime.now()
            
            block1 = Block(titulo=data.get('titutlo'),
                          contenido=data.get('contenido'),
                          fecha_creaccion=fecha 
            )
            block1.save()
            datos_usuario=Block.objects.all()
            return render(request,'datos_usuario.html',{'datos_usuario':datos_usuario})
        else:
            return render(request,'index.html',{'form':form})
    
    
    form_block=FormBlock()  
    return render(request,'index.html',{'form': form_block} )








def segunda_vista(request):
    return render(request,'mi_template.html')







def Datos_usuario(request):
    nombre_de_busqueda =request.GET.get('titulo')
    
    if nombre_de_busqueda:
        listado_uss = Block.objects.filter()
    else:
        datos_usuario=Block.objects.all()
    
    form =BusquedaUss()
    return render(request,'datos_usuario.html',{'datos_usuario':datos_usuario,'form':form})