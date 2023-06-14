from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger
# Create your views here.
# This where the function in urls.py 

def index(request):
    return render(request, "flights/index.html",{
        "flights": Flight.objects.all() #access to display all
    })


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id) #pk = id
    
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passengers": Passenger.objects.exclude(flights=flight).all() #exclude passenger
    })

#add
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
