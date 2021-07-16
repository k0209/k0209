from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from RestaurantApp.models import Reservation
from RestaurantApp.serializers import ReservationSerializer 
from django.core.files.storage import default_storage 

# Create your views here.
@csrf_exempt
def reservationApi(request, id=0):
    if request.method=='GET':
        reservation = Reservation.objects.all()
        reservation_serializer = ReservationSerializer(reservation, many=True)
        return JsonResponse(reservation_serializer.data, safe=False)
    elif request.method=='POST':
            reservation_data=JSONParser().parse(request)
            reservation_serializer = ReservationSerializer(data=reservation_data)
            if reservation_serializer.is_valid():
                reservation_serializer.save()
                return JsonResponse("Addedd Successfully!", safe=False)
            return JsonResponse("Failed to Add.",safe=False)
    elif request.method=='PUT':
            reservation_data = JSONParser().parse(request)
            reservation=Reservation.objects.get(ReservationId=reservation_data['ReservationId'])
            reservation_serializer=ReservationSerializer(reservation, data=reservation_data)
            if reservation_serializer.is_valid():
                reservation_serializer.save()
                return JsonResponse("Updated Successfully!", safe=False)
            return JsonResponse("Failed to Update.",safe=False)
    elif request.method=='DELETE':
            reservation=Reservation.object.get(ReservationDay=id)
            Reservation.delete()
            return JsonResponse("Deleted Successfully!!",safe=False) 

@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name=default_storage.save(file.name,file) 
    return JsonResponse(file_name,safe=False) 
