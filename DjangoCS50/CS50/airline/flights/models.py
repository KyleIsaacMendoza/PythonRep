from django.db import models

# Create your models here.

#Airport
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} ({self.code})"
    
#Flight    
class Flight(models.Model):
    
    #parameter
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    
    
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    
    duration = models.IntegerField()
    
    #every flight have origin, destination, and duration
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    
    
class Passenger(models.Model):
    #properties of passenger have
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    
    #string representation
    def __str__(self):
        return f"{self.first} {self.last}"
    