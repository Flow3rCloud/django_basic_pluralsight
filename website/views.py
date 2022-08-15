from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting


def welcome(request):
    #return HttpResponse('Welcome to my Meetings OnlineApp')

    return render(request, "website/welcome.html",
                  {"num_meetings": Meeting.objects.count()})


def date(request):
    return HttpResponse("Fecha actual: " + str(datetime.now()))


# Please add: An about page that shows some text about yourself
def about(request):
    return HttpResponse("Hecho con <3 durante el curso de Pluralsight.")

