from datetime import time
from email.policy import default

from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=50)
    floor = models.IntegerField()
    room_number = models.IntegerField()
    image = models.ImageField(upload_to='media/imagenes/')

    #para visualizar mejor en pantalla de admin: (y para ver mejor los objetos si los necesito como un str en algún template)
    def __str__(self):
        return f"{self.name} - N° {self.room_number} - Piso: {self.floor}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    # agregar defaults además soluciona el error si ya habíamos creado la tabla sin columnas start_Time/duration
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #si borro un salòn, se borraràn las reuniones
    #django necesita comportamiento on_delete especificado en las foreingn keys


    #para visualizar mejor en admin: (y para ver mejor los objetos si los necesito como un str en algún template)
    def __str__(self):
        return f"{self.title} a las: {self.start_time}, en fecha: {self.date}"