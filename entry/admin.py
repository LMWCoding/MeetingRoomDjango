from django.contrib import admin
from django.utils.translation import gettext_lazy as _
import datetime
import pytz

# Register your models here.
from .models import Meeting,Room

#Custom Filter Function Defined here
class CompletionFilter(admin.SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = _('Completion Status')

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'completion'

    def lookups(self, request, model_admin):
        return (
            ('completed', _('Meeting over')),
            ('on going', _('On going')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'completed':
            return queryset.filter( end__lte = datetime.datetime.now(tz=pytz.UTC))
        if self.value() == 'on going':
            return queryset.filter( start__gte = datetime.datetime.now(tz=pytz.UTC))


# Customise what to list, and the filters
class MeetingAdmin(admin.ModelAdmin):
    list_display = ("custname", "start", "end", "room", )
    #list_filter = ('room', 'start', )
    list_filter = ('room', CompletionFilter , 'start',)
    sortable_by = ('room', 'start', 'end', 'custname')

class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    list_filter = ('location',)

admin.site.register(Meeting, MeetingAdmin)
admin.site.register(Room, RoomAdmin)

