from import_export.widgets import ForeignKeyWidget, DurationWidget, DateWidget, DateTimeWidget
from datetime import timedelta
from numpy import NaN
from pandas import NaT
import uuid
import re

# kwargs = {
#   'row_number': 10, 
#   'file_name': 'Аудит заявок РФ_09.03.23.xlsx', 
#   'user': <SimpleLazyObject: <User:   >>
# }

class TitleForeignKeyWidget(ForeignKeyWidget):
    # Service
    # AdditionalSalesChannel
    # TVPTestType
    # TVPPresence
    # AgentInstaller
    # AgentInstaller
    # IPTVTariffPlan
    # TariffPlan

    def get_queryset(self, value, row, *args, **kwargs):
        obj = self.model.objects.filter(title=value)
        return obj

    def clean(self, value, row=None, **kwargs):
        obj = self.get_queryset(value, row)
        if len(obj) > 0:
            return obj[0]

        if value is None or isinstance(value, float) or isinstance(value, type(NaT)):
            value = 'None'

        new_obj, created = self.model.objects.get_or_create(title=value)
        return new_obj
    

class StatusForeignKeyWidget(ForeignKeyWidget):
    # Status
    def get_queryset(self, value, row, *args, **kwargs):
        obj = self.model.objects.get(title=value)
        return obj

    def clean(self, value, row=None, *args, **kwargs):
        # obj, created = self.model.objects.get_or_create(title=value)
        obj = self.get_queryset(value, row)
        return obj


class ClientForeignKeyWidget(ForeignKeyWidget):
    # Client
    def clean(self, value, row=None, **kwargs):
        INN = row['ИНН']
        if INN is None or value is NaN:
            INN = 0
        obj, created = self.model.objects.get_or_create(title=value, INN=INN)
        return obj


class InstallerForeignKeyWidget(ForeignKeyWidget):
    # Installer
    def clean(self, value, row=None, **kwargs):
        first_name, last_name, surname = 'None', 'None', 'None'
        if value is not None and not isinstance(value, float) and not isinstance(value, type(NaT)):
            first_name, last_name, surname = value.split() 
        obj, created = self.model.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            surname=surname
        )
        return obj


class UserForeignKeyWidget(ForeignKeyWidget):
    # for fields where ForeignKey = User
    def clean(self, value, row=None, **kwargs):
        email = uuid.uuid4().hex[:6].upper() + '@example.com'
        password = '12345'
        first_name, last_name, surname = 'None', 'None', 'None'
        if value is not None and not isinstance(value, float) and not isinstance(value, type(NaT)):
            first_name, last_name, surname = value.split() 
        obj = self.model.objects.filter(
            first_name=first_name, 
            last_name=last_name, 
            surname=surname
        )
        if len(obj) > 0:
            return obj[0]
        
        obj = self.model.objects.create_user(
            email=email,
            password=password,
            first_name=first_name, 
            last_name=last_name, 
            surname=surname
        )
        return obj
    

class ClearDurationWidget(DurationWidget):

    def clean(self, value, row=None, **kwargs):
        if value is None or isinstance(value, float) or isinstance(value, type(NaT)):
            return None
        
        pattern = r'\d+д. \d+ч. \d+м.'
        
        if not re.findall(pattern, str(value)):
            raise ValueError("Enter a valid time.")

        nums = [int(num) for num in re.findall(r'\d+', value)]
        days = nums[0]
        hours = nums[1]
        minutes = nums[2]


        return timedelta(days=days, hours=hours, minutes=minutes)
        
        
class iDateTimeWidget(DateTimeWidget):
    def clean(self, value, row=None, **kwargs):
        if value is NaT or isinstance(value, type(NaT)):
            return None

        return super().clean(value, row, **kwargs)


class iDateWidget(DateWidget):
    def clean(self, value, row=None, **kwargs):
        if value is NaT or isinstance(value, type(NaT)):
            return None

        return super().clean(value, row, **kwargs)
