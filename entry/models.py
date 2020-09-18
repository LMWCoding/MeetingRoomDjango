from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.location} - {self.name}"

class Meeting(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    custname = models.CharField(max_length=64)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")

    def __str__(self):
        return f"{self.start} to {self.end} {self.room.name} {self.custname}"

