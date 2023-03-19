from django.db import models
from users.models import User

from dataclasses import dataclass


class ConnectionRequest(models.Model):
    number = models.PositiveIntegerField(db_index=True, verbose_name='Номер заявки')
    client = models.ForeignKey(
        'Client', related_name='connection_requests', 
        on_delete=models.PROTECT, 
        verbose_name='Клиент'
    )
    status = models.ForeignKey(
        'Status', related_name='connection_requests', 
        on_delete=models.PROTECT,
        verbose_name='Статус заявки'
    )
    date_entered_status = models.DateTimeField(
        verbose_name='Дата входа заявки в статус'
    )
    service = models.ForeignKey(
        'Service', related_name='connection_requests', 
        on_delete=models.PROTECT, 
        verbose_name='Услуга'
    )
    additional_sales_channel = models.ForeignKey(
        'AdditionalSalesChannel', 
        related_name='connection_requests',
        on_delete=models.PROTECT, 
        blank=True, null=True,
        verbose_name='Доп.канал продаж'
    )
    reg_date = models.DateTimeField(verbose_name='Дата регистрации')
    reg_date_for_request = models.DateTimeField(
        null=True, verbose_name='Дата регистрации под заявки'
    )
    reg_date_brigade_for_TVP = models.DateTimeField(
        null=True, verbose_name='Регистрация наряда на ТВП'
    )
    completed_by = models.ForeignKey(
        User, related_name='completed_connection_requests', 
        on_delete=models.PROTECT, 
        blank=True, null=True, 
        verbose_name='Оператор завершивший заявку'
    )
    rejection_date = models.DateTimeField(
        null=True, verbose_name='Дата отклонения под заявки'
    )
    TVP_test_type = models.ForeignKey(
        'TVPTestType', related_name='connection_requests', 
        on_delete=models.PROTECT, null=True, 
        verbose_name='Тип проверки ТВП'
    )
    TVP_presence = models.ForeignKey(
        'TVPPresence', related_name='connection_requests', 
        on_delete=models.PROTECT, null=True, 
        verbose_name='Наличие ТВП'
    )
    completion_TVP_date = models.DateTimeField(
        null=True, verbose_name='Завершение проверки ТВП'
    )
    TVP_check_duration = models.TimeField(
        null=True, verbose_name='Длительность проверки ТВП'
    )
    agreed_connection_date = models.DateTimeField(
        blank=True, null=True, verbose_name='Согласованная дата подключения'
    )
    installer = models.ForeignKey(
        'Installer', related_name='connection_requests', 
        on_delete=models.PROTECT, blank=True, null=True, 
        verbose_name='Инсталлятор'
    )
    agent_installer = models.ForeignKey(
        'AgentInstaller', related_name='connection_requests', 
        on_delete=models.PROTECT, blank=True, null=True, 
        verbose_name='Агент-инсталлятор'
    )
    comment_TVP_ShPD = models.CharField(
        max_length=250, blank=True, verbose_name='Комментарий ТВП ШПД',
        null=True
    )
    started_by = models.ForeignKey(
        User, related_name='started_connection_requests', 
        on_delete=models.PROTECT, blank=True, null=True, 
        verbose_name='Оператор заводивший заявку'
    )
    id_agreement_KURS = models.CharField(
        max_length=250, blank=True, verbose_name='ID Договор КУРС',
        null=True
    )
    note = models.CharField(
        max_length=250, blank=True, verbose_name='Примечание',
        null=True
    )
    contact_phone_number = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='Контактный телефон',  
        default=0
    )
    contact_person = models.CharField(
        max_length=200, blank=True, verbose_name='Контактное лицо',
        null=True
    )
    TP_ShPD_price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, 
        null=True, verbose_name='Стоимость ТП (ШПД)'
    )
    TP_IPTV_price = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, 
        null=True, verbose_name='Стоимость ТП (IPTV)'
    )
    contract_created_by_fio = models.CharField(
        max_length=250, blank=True, 
        verbose_name='ФИО сотрудника создавшего договор',
        null=True
    )
    IPTV_tariff_plan = models.ForeignKey(
        'IPTVTariffPlan', related_name='connection_requests', 
        on_delete=models.PROTECT, blank=True, null=True, 
        verbose_name='Тарифный план IPTV'
    )
    access_card_number = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='Номер карты доступа'
    )
    IPTV_access_card_number = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='Номер карты доступа IPTV'
    )
    tariff_plan = models.ForeignKey(
        'TariffPlan', related_name='connection_requests', 
        on_delete=models.PROTECT, blank=True, null=True, 
        verbose_name='Тарифный план'
    )
    client_number_SUS = models.PositiveIntegerField(
        blank=True, null=True, verbose_name='№ клиентский СУС'
    )
    sending_date_APTV = models.DateTimeField(
        blank=True, null=True, verbose_name='Дата отправки на АПТВ'
    )
    finishing_date_APTV_planned = models.DateTimeField(
        blank=True, null=True, verbose_name='Дата окончания АПТВ планируемая'
    )
    finishing_date_APTV_actual = models.DateTimeField(
        blank=True, null=True, verbose_name='Дата окончания АПТВ фактическая'
    )
    APTV_duration = models.DurationField(
        blank=True, null=True, verbose_name='Длительность этапа АПТВ'
    )
    sending_date_DO = models.DateTimeField(
        blank=True, null=True, verbose_name='Дата отправки на ДО'
    )
    finishing_date_DO_planned = models.DateTimeField(
        blank=True, null=True, verbose_name='Дата окончания ДО планируемая'
    )
    finishing_date_DO_actual = models.DateTimeField(
        blank=True, null=True, verbose_name='Дата окончания ДО фактическая'
    )
    DO_duration = models.DurationField(
        blank=True, null=True, verbose_name='Длительность этапа ДО',
    )

    class Meta:
        verbose_name = 'Заявка на подключение'
        verbose_name_plural = 'Заявки на подключение'
        ordering = ('-date_entered_status',)

    def __str__(self):
        return f"Заявка №{self.number}"


class Client(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название клиента')
    INN = models.PositiveBigIntegerField(db_index=True, verbose_name='ИНН')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.title


class Status(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    group = models.ForeignKey(
        'StatusGroup', related_name='statuses', 
        on_delete=models.PROTECT, verbose_name='Группа'
    )

    class Meta:
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статусы заявок'
        ordering = ('group', 'title')

    def __str__(self):
        return self.title


class StatusGroup(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Группа статуса'
        verbose_name_plural = 'Группы статусов'

    def __str__(self):
        return self.title


class Service(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


class AdditionalSalesChannel(models.Model):
    title = models.CharField(max_length=60, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Доп.канал продажи'
        verbose_name_plural = 'Доп.каналы продажи'

    def __str__(self):
        return self.title


class TVPTestType(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Тип проверки ТВП'
        verbose_name_plural = 'Типы проверок ТВП'

    def __str__(self):
        return self.title


class TVPPresence(models.Model):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Наличие ТВП'
        verbose_name_plural = 'Наличие ТВП'

    def __str__(self):
        return self.title


class Installer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    surname = models.CharField(max_length=50, verbose_name='Отчество')

    class Meta:
        verbose_name = 'Инсталлятор'
        verbose_name_plural = 'Инсталляторы'

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.surname}"


class AgentInstaller(models.Model):
    title = models.CharField(max_length=250, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Агент-инсталлятор'
        verbose_name_plural = 'Агенты-инсталляторы'

    def __str__(self):
        return self.title


class IPTVTariffPlan(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Тарифный план IPTV'
        verbose_name_plural = 'Тарифные планы IPTV'

    def __str__(self):
        return self.title


class TariffPlan(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Тарифный план'
        verbose_name_plural = 'Тарифные планы'

    def __str__(self):
        return self.title

#
# class File(models.Model):
#     title = models.CharField(max_length=256, default='No title', verbose_name='Название')
#     file = models.FileField(upload_to='files', verbose_name='Файл')
#     upload_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
#
#     class Meta:
#         verbose_name = 'Файл .xlsx с заявками'
#         verbose_name_plural = 'Файлы .xlsx с заявками'
#         ordering = ('-upload_at',)
#

@dataclass
class DataExel:
    number: int
    client: str
    inn: int
    status: str
    date_entered_status: str
    service: str
    additional_sales_channel: str
    reg_date: str
    reg_date_for_request: str
    reg_date_brigade_for_TVP: str
    completed_by: str
    rejection_date: str
    TVP_test_type: str
    TVP_presence: str
    completion_TVP_date: str
    TVP_check_duration: str
    agreed_connection_date: str
    installer: str
    agent_installer: str
    comment_TVP_ShPD: str
    started_by: str
    id_agreement_KURS: str
    number_agreement_KURS: str
    note: str
    contact_phone_number: str
    contact_person: str
    TP_ShPD_price: str
    TP_IPTV_price: str
    contract_created_by_fio: str
    IPTV_tariff_plan: str
    access_card_number: str
    IPTV_access_card_number: str
    tariff_plan: str
    client_number_SUS: str
    sending_date_APTV: str
    finishing_date_APTV_planned: str
    finishing_date_APTV_actual: str
    APTV_duration: str
    sending_date_DO: str
    finishing_date_DO_planned: str
    finishing_date_DO_actual: str
    DO_duration: str
