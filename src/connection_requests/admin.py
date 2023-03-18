from django.contrib import admin

from .models import ConnectionRequest, Client, Status, StatusGroup, Service, AdditionalSalesChannel, TVPTestType, \
    TVPPresence, Installer, AgentInstaller, IPTVTariffPlan, TariffPlan


@admin.register(ConnectionRequest)
class ConnectionRequestAdmin(admin.ModelAdmin):
    list_display = ('number', 'status',)
    list_filter = ('status',)
    raw_id_fields = ('client', 'status', 'service', 'additional_sales_channel', 'completed_by', 'TVP_test_type',
                     'TVP_presence', 'installer', 'agent_installer', 'started_by', 'IPTV_tariff_plan')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('title', 'INN')


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('title', 'group')
    list_filter = ('group',)


@admin.register(StatusGroup)
class StatusGroupAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(AdditionalSalesChannel)
class AdditionalSalesChannelAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(TVPTestType)
class TVPTestTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(TVPPresence)
class TVPPresenceAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Installer)
class InstallerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'surname')


@admin.register(AgentInstaller)
class AgentInstallerAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(IPTVTariffPlan)
class IPTVTariffPlanAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(TariffPlan)
class TariffPlanAdmin(admin.ModelAdmin):
    list_display = ('title',)
