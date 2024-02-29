from rest_framework import serializers
from .models import Dht11

class DHT11Serialize(serializers.ModelSerializer):
    class Meta:
        model = Dht11
        fields = '__all__'