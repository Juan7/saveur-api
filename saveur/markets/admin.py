from django.contrib import admin

from . import models


@admin.register(models.Market)
class MarketAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(models.MarketType)
class MarketTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MarketSchedule)
class MarketScheduleAdmin(admin.ModelAdmin):
    list_display = ['market', 'day', 'start_time', 'end_time']
    raw_id_fields = ['market']
