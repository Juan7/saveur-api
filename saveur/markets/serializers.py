from rest_framework import serializers
from django.utils import timezone
from . import models


class MarketTypeSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.MarketType
        fields = ('id', 'name', 'image', 'url_image', 'is_active', 'created_at')


class MarketScheduleSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.MarketSchedule
        fields = ('id', 'day', 'start_time', 'end_time', 'is_active',
                  'created_at')


class MarketSerializer(serializers.ModelSerializer):
    type = MarketTypeSerializer(many=False)
    schedule = MarketScheduleSerializer(many=True, source='marketschedule_set')

    class Meta:

        model = models.Market
        fields = (
            'id',
            'name',
            'short_name',
            'place',
            'description',
            'description2',
            'suggestion',
            'latitude',
            'longitude',
            'type',
            'image',
            'url_image',
            'schedule',
            'is_active',
            'created_at'
        )
