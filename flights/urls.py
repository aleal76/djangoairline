from django.urls import path,include

from . import views

app_name='flights' #to avoid name issues between apps

urlpatterns =  [
    path("", views.index, name="index"),
    path("flights/",views.flights, name="flights"),
]

