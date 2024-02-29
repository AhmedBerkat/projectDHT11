from .models import Dht11
from .serializers import DHT11Serialize
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(["GET", "POST"])
def dhtser(request):
    if request.method == "GET":
        all = Dht11.objects.all()
        dataSer = DHT11Serialize(all, many=True)  # les données se forment fichier JSON
        return Response(dataSer.data)
    elif request.method == "POST":
        serial = DHT11Serialize(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serial.errors, status=status.HTTP_400_CREATED)