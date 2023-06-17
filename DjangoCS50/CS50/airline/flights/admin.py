from django.contrib import admin

#import your classes
from .models import Flight, Airport, Passenger


#You can create your Own Custom Display in local:.../admin

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin", "destination", "duration")


class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)



admin.site.register(Airport) # register Class onto Admin site to make it easy to manage
admin.site.register(Flight, FlightAdmin) #
admin.site.register(Passenger, PassengerAdmin) #