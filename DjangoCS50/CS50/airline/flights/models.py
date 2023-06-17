from django.db import models

# Create your models here.

# Airport Class for code and city
#Airport
class Airport(models.Model): 
    code = models.CharField(max_length=3) # CharField(length) -> code = models is a string
    city = models.CharField(max_length=64) #
    
    def __str__(self):
        return f"{self.city} ({self.code})"
    
#Flight   
class Flight(models.Model):
    # origin = models.CharField(max_length=64) 
    # destination = models.CharField(max_length=64)
    # duration = models.IntegerField()
    # -> before making origin, destination a foreign key
    #parameter
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") #origin is a foreign key
    
    
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals") #destination is a foreign key
    
    duration = models.IntegerField() # duration = model is a string
    
    #every flight have origin, destination, and duration
    def __str__(self):
        #setting string in shell 
        return f"{self.id}: {self.origin} to {self.destination}"
    

# Passenger info such as name, email, and etc
class Passenger(models.Model):
    #properties of passenger have
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    
    #setting a relationship ManyToManyField on flights to use it on other area as well
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    
    #string representation
    def __str__(self):
        return f"{self.first} {self.last}"
    