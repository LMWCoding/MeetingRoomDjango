from django.shortcuts import render
from django.http import HttpResponse
from .models import Meeting, Room

# Create your views here.
def index(request):
    return render(request, "entry/index.html", {
        "meetings": Meeting.objects.all()
    })

