"""meeting_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from meetings.views import detail, rooms_list #importo las funciones de views.py de la app meetings

from website.views import welcome, date, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', welcome, name="welcome"), 
    path('date', date),
    path('about', about),

    # las path con prefijo meetings las llevo al archivo urls.py de la aplicación correspondiente: 

    #path('meetings/<int:id>', detail, name="detail"),
    #path('meetings/rooms', rooms_list, name="rooms"), # primer argumento de path es la url, 2o el nombre de la función en views.py, 3o el nombre para linkear en la sintaxis {% url 'rooms' %} en el template html  
    
    # incluyo las urls de la app (las que comenté arriba)
    path('meetings/', include('meetings.urls')) 
    #1er argumento incluyo los paths de la app meetings con el prefijo "meetings/" 
    #segundo argumento con el include especifico donde buscar el file urls.py (en la app meetings)
    

]