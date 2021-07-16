from rest_framework import serializers  
from RestaurantApp.models import Reservation, Contactus 


class ReservationSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Reservation  
        fields = (  'ReservationId',
                    'ReservationDay',
                    'ReservationHour', 
                    'Name', 
                    'Phonenumber',
                    'Numberofpersons')

class ContactusSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Contactus 
        
