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

#    currentMtg = Meeting.objects.filter( room = room.id )
#    currentMtg = Meeting.objects.filter( room = room.id  , start__lte= datetime.datetime.now()).exclude( end__lte= datetime.datetime.now())
    currentMtg = Meeting.objects.filter( room = room.id  , start__lte= datetime.datetime.now(tz=pytz.UTC),  end__gte= datetime.datetime.now(tz=pytz.UTC))
    nextMtg = Meeting.objects.filter(room = room.id, start__gte = datetime.datetime.now(tz=pytz.UTC), end__gte = datetime.datetime.now(tz=pytz.UTC)).order_by('start')

    if (len(currentMtg)  != 0 ):
        # assumption is there is only one match.  The data entry should be clean, have no duplicate usage of room
        return render(request, "signage/roomoccupied.html", { "custname" : currentMtg[0].custname, "roomname" : selectedRoom })
    else: 
        if (len(nextMtg) != 0):
            # if upcoming mtg is in an hour, show
            # nextMtgTime = nextMtg[0].start
            # currentTime = datetime.datetime.now(tz=pytz.UTC)
            timeToNextMtg = nextMtg[0].start - datetime.datetime.now(tz=pytz.UTC)
            if (timeToNextMtg < datetime.timedelta(minutes=15)):
                # Meeeting in next 15 min
                return render(request, "signage/roomoccupied.html", { "custname" : nextMtg[0].custname, "roomname" : nextMtg[0].room.name})
            elif (timeToNextMtg < datetime.timedelta(hours=1)):
                # Meeeting in next 1 hr
                return render(request, "signage/roomfree.html", { "message" : f"{int(timeToNextMtg.seconds/60)}min to next mtg", "roomname" : selectedRoom})
        # more than an hour gap, or no next mtg found
        return render(request, "signage/roomfree.html", { "message" : "g'Day", "roomname" : selectedRoom})



def roommanual(request, location, roomname, custname):
#    selectedLocation = location
    selectedRoom = roomname


    if (custname  != "..." ):
        # assumption is there is only one match.  The data entry should be clean, have no duplicate usage of room

        # print(custname)

        return render(request, "signage/roomoccupied.html", { "custname" : custname, "roomname" : selectedRoom })
    else: 
        return render(request, "signage/roomfree.html", { "message" : "g'Day", "roomname" : selectedRoom})