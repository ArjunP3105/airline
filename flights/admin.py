from django.contrib import admin

from .models import Flights,airport,passenger
# Register your models here.
class Flightadmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")

class AirportAdmin(admin.ModelAdmin):
    list_display = ("id","code","city")

class passengeradmin(admin.ModelAdmin):
    list_display = ("id","first","last")
    filter_horizontal = ("flights",)

admin.site.register(airport,AirportAdmin)
admin.site.register(Flights,Flightadmin)
admin.site.register(passenger,passengeradmin)