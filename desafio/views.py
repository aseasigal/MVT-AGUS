from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Prueba

# Create your views here.

def una_vista(request):
    return HttpResponse('<h1>Mi perro dinamita</h1>')

def un_template(request):
    
    template = loader.get_template('index.html')
    
    prueba1= Prueba(nombre='Pepito')
    prueba2= Prueba(nombre='Julepe')
    prueba3= Prueba(nombre='Ricardo')
    prueba1.save()
    prueba2.save()
    prueba3.save()
    
    
    # render = template.render({'lista_objetos':[prueba1,prueba2,prueba3]})
    # return HttpResponse('<h1>otra cosa</h1>')
    return render(request,'index.html',{'lista_objetos':[prueba1,prueba2,prueba3]})