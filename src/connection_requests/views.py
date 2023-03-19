from django.http.response import HttpResponse
import pandas as pd

from .resources import ConnectionRequestResources
from tablib import Dataset


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

    return pd.read_excel(file_path)[columns]


def index(r):
    connection_resources = ConnectionRequestResources()
    df = read_exel(r'./Аудит заявок РФ_09.03.23.xlsx')
    dataset = Dataset().load(df)
    result = connection_resources.import_data(dataset=dataset, dry_run=True) # Test the data import

    if not result.has_errors():
        connection_resources.import_data(dataset=dataset, dry_run=False)  # Actually import now
    else:
        for i, err in result.row_errors():
            print(1, err[0])

    return HttpResponse('Heallo')