from django.db import models

# Create your models here.
class Reservation(models.Model):
    ReservationId = models.AutoField(primary_key=True, auto_created = True)
    ReservationDay= models.CharField(max_length=20, default="Today")
    ReservationHour= models.CharField(max_length=20, default="9:00 PM")
    Name= models.CharField(max_length=50, default="Anonymous")
    Phonenumber= models.CharField(max_length=15, default="Not Disclosed")
    Numberofpersons= models.IntegerField(default=1)

class Contactus(models.Model): 
    Emp= models.AutoField(primary_key=True) 
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)
