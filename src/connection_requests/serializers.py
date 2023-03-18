from rest_framework import serializers

from .models import ConnectionRequest


class ConnectionRequestListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionRequest
        fields = ('id', 'number', 'client', 'status')
        depth = 2


class ConnectionRequestRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionRequest
        fields = '__all__'
        depth = 2


class ConnectionRequestProcessingHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectionRequest
        fields = ('status', 'date_entered_status', 'reg_date_brigade_for_TVP', 'completion_TVP_date',
                  'TVP_check_duration', 'sending_date_APTV', 'finishing_date_APTV_planned',
                  'finishing_date_APTV_actual', 'APTV_duration', 'sending_date_DO', 'finishing_date_DO_planned',
                  'finishing_date_DO_actual', 'DO_duration')
        depth = 2
