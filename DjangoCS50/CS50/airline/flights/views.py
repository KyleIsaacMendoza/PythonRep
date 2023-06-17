from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger #import class that you will use
# Create your views here. 
# This where the function in urls.py 

def index(request):
    return render(request, "flights/index.html",{
        "flights": Flight.objects.all() #access to display all objects in class Flight
    })


# flight_id = flight table main id
def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id) #pk = main id of flight
    
    return render(request, "flights/flight.html", {
        "flight": flight, # flight = Flight class
        "passengers": flight.passengers.all(), #access to passenger
        "non_passengers": Passenger.objects.exclude(flights=flight).all() #exclude Passenger class to exclude
    })

#This will add a flight in tablef.
#this will run if the form is submitted
#add book
def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        
        #access class passenger > flights object and then add the data on flight
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))
