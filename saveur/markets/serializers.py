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


class MarketRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MarketRate
        fields = (
            'user',
            'market',
            'type',
            'rate'
        )


class MerchantRateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MerchantRate
        fields = (
            'user',
            'merchant',
            'type',
            'rate'
        )


class MarketMinSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.Market
        fields = (
            'id',
            'name',
            'short_name',
            'place',
            'is_active',
            'created_at'
        )


class MarketSerializer(serializers.ModelSerializer):
    type = MarketTypeSerializer(many=False)
    schedule = MarketScheduleSerializer(many=True, source='marketschedule_set')
    rate = serializers.SerializerMethodField()

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
            'rate',
            'url_image',
            'schedule',
            'is_active',
            'created_at'
        )

    def get_rate(self, obj):
        if self.context['request'].user:
            data = obj.marketrate_set.filter(user=self.context['request'].user)
        else:
            data = obj.marketrate_set.values('market', 'type').aggregate(rate=Avg('rate'))
            data = list(data)
        return MarketRateSerializer(data=data, many=True)

class MerchantScheduleSerializer(serializers.ModelSerializer):

    class Meta:

        model = models.MerchantSchedule
        fields = ('id', 'day', 'start_time', 'end_time', 'is_active',
                  'created_at')


class MerchantSerializer(serializers.ModelSerializer):
    market = MarketMinSerializer(many=False)
    type = MarketTypeSerializer(many=False)
    schedule = MerchantScheduleSerializer(many=True, source='merchantschedule_set')
    rate = serializers.SerializerMethodField()

    class Meta:

        model = models.Market
        fields = (
            'id',
            'market',
            'name',
            'description',
            'description2',
            'suggestion',
            'type',
            'rate',
            'image',
            'url_image',
            'schedule',
            'is_active',
            'created_at'
        )

    def get_rate(self, obj):
        if self.context['request'].user:
            data = obj.merchantrate_set.filter(user=self.context['request'].user)
        else:
            data = obj.merchantrate_set.values('merchant', 'type').aggregate(rate=Avg('rate'))
            data = list(data)
        return MerchantRateSerializer(data=data, many=True).data
