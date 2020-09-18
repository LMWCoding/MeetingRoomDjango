from django.contrib import admin

# Register your models here.
from .models import Meeting,Room
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("room", "start", "end", "custname")
    list_filter = ('room', 'start')
    sortable_by = ('room', 'start', 'end', 'custname')

class RoomAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Room, RoomAdmin)