from django.shortcuts import render, get_object_or_404

from .models import Meeting, Room #importo los modelos de la app meetings

def detail(request, id): #id es la clave primaria de la tabla Meeting
    #meeting = Meeting.objects.get(pk=id) # pk = primary key - busca la fila con el id dado
    meeting = get_object_or_404(Meeting, pk=id) #se pasa primero la tabla y luego el id
    return render(request, "meetings/details.html", {"meeting": meeting})

def rooms_list(request):
    rooms = Room.objects.all()
    return render(request, "meetings/rooms.html", {"rooms": rooms})

