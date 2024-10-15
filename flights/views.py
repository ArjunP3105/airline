from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from .models import Flights,passenger
 
# Create your views here
def index(request):
    return render(request,"flights/index.html",{
        "flights":Flights.objects.all()
    })

def flight(request,flight_id):
    flight = Flights.objects.get(pk = flight_id)
    return render(request,"flights/flight.html",{
        "flight":flight,
        "passengers":flight.passengers.all(),# we use flight.object.all than passenger as we want the passeger for this particular flight and not all passengers in the table
        "non_passenger":passenger.objects.exclude(flights = flight).all()
    })


def book(request,flight_id):
    if request.method == "POST":
        flight = Flights.objects.get(pk = flight_id)
        #we ask the user to input the id of the passenger
        Passenger = passenger.objects.get(pk = int(request.POST["passenger"]))
        Passenger.flights.add(flight) #adding entire flight information
        return HttpResponseRedirect(reverse("flight",args=(flight.id)))
