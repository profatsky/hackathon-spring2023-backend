import datetime

from django.http import Http404
from django.http.response import HttpResponse
from django.utils import timezone
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import pandas as pd
from pandas import NaT
from tablib import Dataset
import numpy as np


from .models import ConnectionRequest
from .serializers import ConnectionRequestListSerializer, ConnectionRequestRetrieveSerializer, \
    ConnectionRequestProcessingHistorySerializer
from .resources import ConnectionRequestResources


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

    @action(detail=False, methods=['get'])
    def history(self, request):
        number = request.GET.get('number')
        if not number:
            raise Http404()
        queryset = ConnectionRequest.objects.filter(number=number).order_by('date_entered_status')
        serializer = ConnectionRequestProcessingHistorySerializer(queryset, many=True)
        return Response(serializer.data)

      
      

def read_exel(file_path: str) -> pd.DataFrame:
    columns = [
        'Номер заявки', 'Клиент*', 'ИНН', 
        'Статус', 'Дата входа заявки в статус', 'Услуга',
        'Доп. канал продаж', 'Дата регистрации заявки', 
        'Дата регистрации под заявки', 'Рег. наряда на ТВП',
        'Оператор завершивший заявку', 'Дата отклонения под заявки',
        'Тип проверки ТВП', 'Наличие ТВП', 
        'Завершение проверки ТВП', 'Длит. проверки ТВП',
        'Согласованная дата подкл.',
        'Инсталятор', 'Агент-инсталлятор',
        'Комментарий ТВП ШПД', 'Оператор заводивший заявку',
        'ID Договор КУРС', 'Примечание', 'Контактный телефон', 
        'Контактное лицо', 'Стоимость ТП (ШПД)', 
        'Стоимость ТП (IPTV)', 'ФИО сотрудника, создавшего договор',
        'Тарифный план IPTV', 'Номер карты доступа', 
        'Номер карты доступа IPTV', 'Тарифный план',
        '№ клиентский СУС', 'Дата отправки на АПТВ', 'Дата окончания АПТВ планируемая',
        'Дата окончания АПТВ фактическая', 'Длительность этапа АПТВ',
        'Дата отправки на ДО', 'Дата окончания ДО планируемая',
        'Дата окончания ДО фактическая', 'Длительность этапа ДО'
    ]

    return pd.read_excel(file_path)[columns].replace(
        {np.nan: 0.0, NaT: pd.Timestamp(0)}
    )


def index(r):
    connection_resources = ConnectionRequestResources()
    df = read_exel(r'./Аудит заявок РФ_10.03.23.xlsx')
    dataset = Dataset().load(df)
    # print('===================================')
    # print(dataset[1])
    # print('===================================')
    result = connection_resources.import_data(dataset=dataset, dry_run=True) # Test the data import

    if not result.has_errors():
        connection_resources.import_data(dataset=dataset, dry_run=False)  # Actually import now
    else:
        for i, err in result.row_errors()[:1]:
            print(i, err[0].traceback)
            print(i, err[0].error)
            # print(i, err[0].row)

    return HttpResponse('Heallo')
