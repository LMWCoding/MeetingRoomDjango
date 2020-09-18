from django.urls import path

from . import views

app_name = "signage"
urlpatterns = [
    path("", views.index, name="index"),
#    path("singapore/1", views.room1, name="room1")
    path("<str:location>/<str:roomname>", views.roomauto, name="roomauto"),
    path("<str:location>/<str:roomname>/<str:custname>", views.roommanual, name="roommanul")
    
]