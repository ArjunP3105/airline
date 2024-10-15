from django.db import models

# Create your models here.
#models are always classes in django
class airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length= 64)

    def __str__(self):
        return f"{self.city}({self.code})"
    

class Flights(models.Model): #we define te colums in our table
    origin = models.ForeignKey(airport,on_delete = models.CASCADE , related_name= "departure")
    # since we already have an airpot table we want the dest and origin to take data frok that and its done using models.foreignkey(airport)
    #on_delete = models.cascade tells us what to do if the data in the airport  gets deleted so all the other flights with that dest/orign is deleted
    # related_name is to reverse search the particular flight   
    destination = models.ForeignKey(airport,on_delete=models.CASCADE,related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    
    def is_valid_flight(self):
        return self.origin != self.destination and self.duration >= 0
    
class passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flights,blank= True,related_name= "passengers")

    def __str__(self):
        return f"{self.first} {self.last}"
