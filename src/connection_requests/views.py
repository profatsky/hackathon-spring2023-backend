import datetime

from django.http import Http404
from django.utils import timezone
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import ConnectionRequest
from .serializers import ConnectionRequestListSerializer, ConnectionRequestRetrieveSerializer, \
    ConnectionRequestProcessingHistorySerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ConnectionRequestViewSet(mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               viewsets.GenericViewSet):
    queryset = ConnectionRequest.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        paginator = PageNumberPagination()

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

        result_page = paginator.paginate_queryset(queryset, request)
        # serializer = ConnectionRequestListSerializer(queryset[:100], many=True)
        serializer = ConnectionRequestListSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        serializer = ConnectionRequestRetrieveSerializer(self.queryset.get(pk=self.kwargs.get('pk')))
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def history(self, request):
        number = request.GET.get('number')
        if not number:
            raise Http404()
        queryset = ConnectionRequest.objects.filter(number=number).order_by('date_entered_status')
        serializer = ConnectionRequestProcessingHistorySerializer(queryset, many=True)
        return Response(serializer.data)
