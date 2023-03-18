import datetime

from django.utils import timezone
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import ConnectionRequest
from .serializers import ConnectionRequestListSerializer, ConnectionRequestRetrieveSerializer


class ConnectionRequestViewSet(mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               viewsets.GenericViewSet):
    queryset = ConnectionRequest.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if INN_filter := self.request.GET.get('inn'):
            queryset = queryset.filter(client__INN=INN_filter)
        elif title := self.request.GET.get('title'):
            queryset = queryset.filter(client__title__icontains=title.replace('+', ' '))
        elif number := self.request.GET.get('number'):
            queryset = queryset.filter(number=number)

        if self.request.GET.get('5-days-no-change'):
            queryset = queryset.distinct().filter(
                date_entered_status__lt=(timezone.now() - datetime.timedelta(days=5))
            )
        if self.request.GET.get('started-by-me'):
            queryset = queryset.distinct().filter(started_by=self.request.user.pk)
        serializer = ConnectionRequestListSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        serializer = ConnectionRequestRetrieveSerializer(self.queryset.get(pk=self.kwargs.get('pk')))
        return Response(serializer.data)
