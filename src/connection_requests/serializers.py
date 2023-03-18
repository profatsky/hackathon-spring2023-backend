from rest_framework import serializers

from .models import ConnectionRequest


class ConnectionRequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionRequest
        fields = ('number', 'client', 'status')
        depth = 2


class ConnectionRequestRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionRequest
        fields = '__all__'
        depth = 2
