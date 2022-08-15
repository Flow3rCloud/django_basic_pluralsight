from django.shortcuts import render

from .models import Meeting

def detail(request, id): #id es la clave primaria de la tabla Meeting
    meeting = Meeting.objects.get(pk=id) # pk = primary key - busca la fila con el id dado
    return render(request, "meetings/details.html", {"meeting": meeting})

