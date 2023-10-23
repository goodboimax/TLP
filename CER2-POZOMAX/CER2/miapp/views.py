from django.shortcuts import render
from django.http import HttpResponse
from .models import Entidad, Comunicado

# Create your views here.

def cards(request):
    title = "Inicio"
    entidades = Entidad.objects.all()
    comunicados = Comunicado.objects.all()
    entidad_combobox = request.GET.get("Entidad")
    print()
    print(entidad_combobox)
    print(request)
    print()
    if entidad_combobox == 'Todos' or entidad_combobox is None:
        comunicados = Comunicado.objects.all()
    else:
        entidad_filtrar = Entidad.objects.get(nombre=entidad_combobox)
        comunicados = Comunicado.objects.filter(Entidad=entidad_filtrar)


    
    data = {
        "comunicados":comunicados,
        "entidades":entidades,
        "title": title,
        "entidad_combobox": entidad_combobox 

    }


    return render(request,'miapp/cards.html', data)

