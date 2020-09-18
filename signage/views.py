from django.shortcuts import render
from django.urls import reverse

import datetime
import pytz

utc=pytz.UTC

from entry.models import Meeting, Room
# Create your views here.
def index(request):
    rooms = Room.objects.all()
    print(rooms)
    return render(request, "signage/index.html", {"roomList" : rooms})


def roomauto(request, location, roomname):
    selectedLocation = location
    selectedRoom = roomname

    try:
        room = Room.objects.get ( name = selectedRoom, location = selectedLocation)
    except:
        return render(request, "signage/roomnotfound.html")

#     currentMtg = Meeting.objects.filter( room = room.id )
#    currentMtg = Meeting.objects.filter( room = room.id  , start__lte= datetime.datetime.now()).exclude( end__lte= datetime.datetime.now())

    currentMtg = Meeting.objects.filter( room = room.id  , start__lte= datetime.datetime.now(tz=pytz.UTC),  end__gte= datetime.datetime.now(tz=pytz.UTC))

    

    if (len(currentMtg)  != 0 ):
        # assumption is there is only one match.  The data entry should be clean, have no duplicate usage of room
        custname =  (currentMtg[0].custname)
        # print(custname)
        # print (currentMtg[0].room.location)
        # print (currentMtg[0].room.name)
        
        return render(request, "signage/roomoccupied.html", { "custname" : custname, "roomname" : selectedRoom })
    else: 
        return render(request, "signage/roomfree.html", { "roomname" : selectedRoom})


def roommanual(request, location, roomname, custname):
#    selectedLocation = location
    selectedRoom = roomname


    if (custname  != "..." ):
        # assumption is there is only one match.  The data entry should be clean, have no duplicate usage of room

        # print(custname)

        return render(request, "signage/roomoccupied.html", { "custname" : custname, "roomname" : selectedRoom })
    else: 
        return render(request, "signage/roomfree.html",  {"roomname" : selectedRoom })