from django.db import models

from users.models import User


class ConnectionRequest(models.Model):
    number = models.PositiveIntegerField(db_index=True, verbose_name='Номер заявки')
    client = models.ForeignKey('Client', related_name='connection_requests', on_delete=models.PROTECT,
                               verbose_name='Клиент')
    status = models.ForeignKey('Status', related_name='connection_requests', on_delete=models.PROTECT,
                               verbose_name='Статус заявки')
    date_entered_status = models.DateTimeField(verbose_name='Дата входа заявки в статус')
    service = models.ForeignKey('Service', related_name='connection_requests', on_delete=models.PROTECT,
                                verbose_name='Услуга')
    additional_sales_channel = models.ForeignKey('AdditionalSalesChannel', related_name='connection_requests',
                                                 on_delete=models.PROTECT, blank=True, null=True,
                                                 verbose_name='Доп.канал продаж')
    reg_date = models.DateTimeField(verbose_name='Дата регистрации')
    reg_date_for_request = models.DateTimeField(null=True, verbose_name='Дата регистрации под заявки')
    reg_date_brigade_for_TVP = models.DateTimeField(null=True, verbose_name='Регистрация наряда на ТВП')
    completed_by = models.ForeignKey(User, related_name='completed_connection_requests', on_delete=models.PROTECT,
                                     blank=True, null=True, verbose_name='Оператор завершивший заявку')
    rejection_date = models.DateTimeField(null=True, verbose_name='Дата отклонения под заявки')
    TVP_test_type = models.ForeignKey('TVPTestType', related_name='connection_requests', on_delete=models.PROTECT,
                                      null=True, verbose_name='Тип проверки ТВП')
    TVP_presence = models.ForeignKey('TVPPresence', related_name='connection_requests', on_delete=models.PROTECT,
                                     null=True, verbose_name='Наличие ТВП')
    completion_TVP_date = models.DateTimeField(null=True, verbose_name='Завершение проверки ТВП')
    TVP_check_duration = models.TimeField(null=True, verbose_name='Длительность проверки ТВП')
    agreed_connection_date = models.DateTimeField(blank=True, null=True, verbose_name='Согласованная дата подключения')
    installer = models.ForeignKey('Installer', related_name='connection_requests', on_delete=models.PROTECT, blank=True,
                                  null=True, verbose_name='Инсталлятор')
    agent_installer = models.ForeignKey('AgentInstaller', related_name='connection_requests', on_delete=models.PROTECT,
                                        blank=True, null=True, verbose_name='Агент-инсталлятор')
    comment_TVP_ShPD = models.CharField(max_length=250, blank=True, verbose_name='Комментарий ТВП ШПД')
    started_by = models.ForeignKey(User, related_name='started_connection_requests', on_delete=models.PROTECT,
                                   blank=True, null=True, verbose_name='Оператор заводивший заявку')
    id_agreement_KURS = models.CharField(max_length=250, blank=True, verbose_name='ID Договор КУРС')
    note = models.CharField(max_length=250, blank=True, verbose_name='Примечание')
    contact_phone_number = models.PositiveIntegerField(blank=True, null=True, verbose_name='Контактный телефон')
    contact_person = models.CharField(max_length=200, blank=True, verbose_name='Контактное лицо')
    TP_ShPD_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True,
                                        verbose_name='Стоимость ТП (ШПД)')
    TP_IPTV_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True,
                                        verbose_name='Стоимость ТП (IPTV)')
    contract_created_by_fio = models.CharField(max_length=250, blank=True,
                                               verbose_name='ФИО сотрудника создавшего договор')
    IPTV_tariff_plan = models.ForeignKey('IPTVTariffPlan', related_name='connection_requests', on_delete=models.PROTECT,
                                         blank=True, null=True, verbose_name='Тарифный план IPTV')
    access_card_number = models.PositiveIntegerField(blank=True, null=True, verbose_name='Номер карты доступа')
    IPTV_access_card_number = models.PositiveIntegerField(blank=True, null=True,
                                                          verbose_name='Номер карты доступа IPTV')
    tariff_plan = models.ForeignKey('TariffPlan', related_name='connection_requests', on_delete=models.PROTECT,
                                    blank=True, null=True, verbose_name='Тарифный план')
    client_number_SUS = models.PositiveIntegerField(blank=True, null=True, verbose_name='№ клиентский СУС')
    sending_date_APTV = models.DateTimeField(blank=True, null=True, verbose_name='Дата отправки на АПТВ')
    finishing_date_APTV_planned = models.DateTimeField(blank=True, null=True,
                                                       verbose_name='Дата окончания АПТВ планируемая')
    finishing_date_APTV_actual = models.DateTimeField(blank=True, null=True,
                                                      verbose_name='Дата окончания АПТВ фактическая')
    APTV_duration = models.TimeField(blank=True, null=True, verbose_name='Длительность этапа АПТВ')
    sending_date_DO = models.DateTimeField(blank=True, null=True, verbose_name='Дата отправки на ДО')
    finishing_date_DO_planned = models.DateTimeField(blank=True, null=True,
                                                     verbose_name='Дата окончания ДО планируемая')
    finishing_date_DO_actual = models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания ДО фактическая')
    DO_duration = models.TimeField(blank=True, null=True, verbose_name='Длительность этапа ДО')

    class Meta:
        verbose_name = 'Заявка на подключение'
        verbose_name_plural = 'Заявки на подключение'
        ordering = ('-date_entered_status',)

    def __str__(self):
        return f"Заявка №{self.number}"


class Client(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название клиента')
    INN = models.PositiveBigIntegerField(db_index=True, unique=True, verbose_name='ИНН')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.title


class Status(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    group = models.ForeignKey('StatusGroup', related_name='statuses', on_delete=models.PROTECT, verbose_name='Группа')

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
    title = models.CharField(max_length=10, unique=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Тип проверки ТВП'
        verbose_name_plural = 'Типы проверок ТВП'

    def __str__(self):
        return self.title


class TVPPresence(models.Model):
    title = models.CharField(max_length=10, unique=True, verbose_name='Название')

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
