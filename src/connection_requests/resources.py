from import_export import resources
from import_export.fields import *
from import_export.widgets import DateWidget, DateTimeWidget, TimeWidget
from .models import *
from .widgets import *


class ConnectionRequestResources(resources.ModelResource):
    number = Field(
        column_name='Номер заявки',
        attribute='number'
    )
    client = Field(
        column_name='Клиент*',
        attribute='client',
        widget=ClientForeignKeyWidget(Client, 'title')
    )
    inn = Field(
        column_name='ИНН',
        attribute='INN'
    )
    status = Field(
        column_name='Статус',
        attribute='status',
        widget=StatusForeignKeyWidget(Status, 'title')
    )
    date_entered_status = Field(
        column_name='Дата входа заявки в статус',
        attribute='date_entered_status',
        widget=DateWidget(
            format='%d/%m/%Y'
        )
    )
    service = Field(
        column_name='Услуга',
        attribute='service',
        widget=TitleForeignKeyWidget(Service, 'title')
    )
    additional_sales_channel = Field(
        column_name='Доп. канал продаж',
        attribute='additional_sales_channel',
        widget=TitleForeignKeyWidget(AdditionalSalesChannel, 'title')
    )
    reg_date = Field(
        column_name='Дата регистрации заявки',
        attribute='reg_date',
        widget=DateWidget(
            format='%d/%m/%Y'
        )
    )
    reg_date_for_request = Field(
        column_name='Дата регистрации под заявки',
        attribute='reg_date_for_request',
        widget=DateWidget(
            format='%d/%m/%Y'
        )
    )
    reg_date_brigade_for_TVP = Field(
        column_name='Рег. наряда на ТВП',
        attribute='reg_date_brigade_for_TVP',
        widget=DateWidget(
            format='%d/%m/%Y'
        )
    )
    completed_by = Field(
        column_name='Оператор завершивший заявку',
        attribute='completed_by',
        widget=UserForeignKeyWidget(User, 'full_name')
    )
    rejection_date = Field(
        column_name='Дата отклонения под заявки',
        attribute='rejection_date',
        widget=DateTimeWidget(
            format='%d/%m/%Y %H:%M'
        )
    )
    TVP_test_type = Field(
        column_name='Тип проверки ТВП',
        attribute='TVP_test_type',
        widget=TitleForeignKeyWidget(TVPTestType, 'title')
    )
    TVP_presence = Field(
        column_name='Наличие ТВП',
        attribute='TVP_presence',
        widget=TitleForeignKeyWidget(TVPPresence, 'title')
    )
    completion_TVP_date = Field(
        column_name='Завершение проверки ТВП',
        attribute='completion_TVP_date',
        widget=DateTimeWidget(
            format='%d/%m/%Y %H:%M'
        )
    )
    TVP_check_duration = Field(
        column_name='Длит. проверки ТВП',
        attribute='TVP_check_duration',
        widget=TimeWidget()
    )
    agreed_connection_date = Field(
        column_name='Согласованная дата подкл.',
        attribute='agreed_connection_date'
    )
    installer = Field(
        column_name='Инсталятор',
        attribute='installer',
        widget=InstallerForeignKeyWidget(Installer, 'full_name')
    )
    agent_installer = Field(
        column_name='Агент-инсталлятор',
        attribute='agent_installer',
        widget=TitleForeignKeyWidget(AgentInstaller, 'title')
    )
    comment_TVP_ShPD = Field(
        column_name='Комментарий ТВП ШПД',
        attribute='comment_TVP_ShPD'
    )
    started_by = Field(
        column_name='Оператор заводивший заявку',
        attribute='started_by',
        widget=UserForeignKeyWidget(User, 'full_name')
    )
    id_agreement_KURS = Field(
        column_name='ID Договор КУРС',
        attribute='id_agreement_KURS'
    )
    note = Field(
        column_name='Примечание',
        attribute='note'
    )
    contact_phone_number = Field(
        column_name='Контактный телефон',
        attribute='contact_phone_number'
    )
    contact_person = Field(
        column_name='Контактное лицо',
        attribute='contact_person'
    )
    TP_ShPD_price = Field(
        column_name='Стоимость ТП (ШПД)',
        attribute='TP_ShPD_price'
    )
    TP_IPTV_price = Field(
        column_name='Стоимость ТП (IPTV)',
        attribute='TP_IPTV_price'
    )
    contract_created_by_fio = Field(
        column_name='ФИО сотрудника, создавшего договор',
        attribute='contract_created_by_fio'
    )
    IPTV_tariff_plan = Field(
        column_name='Тарифный план IPTV',
        attribute='IPTV_tariff_plan',
        widget=TitleForeignKeyWidget(IPTVTariffPlan, 'title')
    )
    access_card_number = Field(
        column_name='Номер карты доступа',
        attribute='access_card_number'
    )
    IPTV_access_card_number = Field(
        column_name='Номер карты доступа IPTV',
        attribute='IPTV_access_card_number'
    )
    tariff_plan = Field(
        column_name='Тарифный план',
        attribute='tariff_plan',
        widget=TitleForeignKeyWidget(TariffPlan, 'title')
    )
    client_number_SUS = Field(
        column_name='№ клиентский СУС',
        attribute='client_number_SUS'
    )
    sending_date_APTV = Field(
        column_name='Дата отправки на АПТВ',
        attribute='sending_date_APTV',
        widget=DateTimeWidget(
            format='%d/%m/%Y %H:%M'
        )
    )
    finishing_date_APTV_planned = Field(
        column_name='Дата окончания АПТВ планируемая',
        attribute='finishing_date_APTV_planned',
        widget=DateTimeWidget(
            format='%d/%m/%Y %H:%M'
        )
    )
    finishing_date_APTV_actual = Field(
        column_name='Дата окончания АПТВ фактическая',
        attribute='finishing_date_APTV_actual',
        widget=DateTimeWidget(
            format='%d/%m/%Y %H:%M'
        )
    )
    APTV_duration = Field(
        column_name='Длительность этапа АПТВ',
        attribute='APTV_duration',
        widget=TimeWidget(
            format='%dd. %Hh. %Mm.'
        )
    )
    sending_date_DO = Field(
        column_name='Дата отправки на ДО',
        attribute='sending_date_DO',
        widget=DateTimeWidget(
            format='%d/%m/%Y %H:%M'
        )
    )
    finishing_date_DO_planned = Field(
        column_name='Дата окончания ДО планируемая',
        attribute='finishing_date_DO_planned',
        widget=DateTimeWidget(
            format='%d/%m/%Y %H:%M'
        )
    )
    finishing_date_DO_actual = Field(
        column_name='Дата окончания ДО фактическая',
        attribute='finishing_date_DO_actual',
        widget=DateTimeWidget(
            format='%d/%m/%Y %H:%M'
        )
    )
    DO_duration = Field(
        column_name='Длительность этапа ДО',
        attribute='DO_duration',
        widget=TimeWidget(
            format='%dd. %Hh. %Mm.'
        )
    )


    class Meta:
        model = ConnectionRequest
        exclude = ['id']
        import_id_fields = ['number']
