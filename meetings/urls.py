from django.urls import path 
from . import views
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
    #estos paths están incluidos en el archivo urls.py del proyecto, con el prefijo meetings/ 
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.rooms_list, name="rooms"), # primer argumento es la url, 2o el nombre de la función en views.py, 
    #3o el nombre para linkear en la sintaxis {% url 'rooms' %} en el template html  
    # path('meetings/', include('meetings.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
