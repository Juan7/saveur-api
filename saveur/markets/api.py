import django_filters

from rest_framework import decorators, permissions, response, status, viewsets, filters

# from main import pagination
from . import models, serializers


class MarketViewSet(viewsets.ModelViewSet):

    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.MarketSerializer

    # pagination_class = pagination.StandardResultsSetPagination
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter)
    queryset = models.Market.objects.filter(is_active=True)

    filter_fields = {
        'name': ['icontains'],
    }

    @decorators.action(
        methods=['post'],
        detail=True,
        url_path='rate-market',
        url_name='api_rate_market',
        permission_classes=[permissions.IsAuthenticated])
    def rate_market(self, request, pk=None):
        instance = self.get_object()
        rate = serializers.MarketRateSerializer(
            data=request.data, many=False)
        rate.is_valid()
        rate_data = rate.data

        models.MarketRate.objects.update_or_create(user=request.user, type=rate_data['type'], market=instance, defaults={'rate': rate_data['rate']})

        result = {
            'message': 'Rated!'
        }
        return response.Response(result ,status=status.HTTP_200_OK)



class MerchantViewSet(viewsets.ModelViewSet):

    # permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.MerchantSerializer

    # pagination_class = pagination.StandardResultsSetPagination
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter)
    queryset = models.Merchant.objects.filter(is_active=True)

    filter_fields = {
        'name': ['icontains'],
        'market': ['exact'],
    }

    @decorators.action(
        methods=['post'],
        detail=True,
        url_path='rate-merchant',
        url_name='api_rate_merchant',
        permission_classes=[permissions.IsAuthenticated])
    def rate_market(self, request, pk=None):
        instance = self.get_object()
        rate = serializers.MerchantRateSerializer(
            data=request.data, many=False)
        rate.is_valid()
        rate_data = rate.data

        models.MerchantRate.objects.update_or_create(user=request.user, type=rate_data['type'], merchant=instance, defaults={'rate': rate_data['rate']})

        result = {
            'message': 'Rated!'
        }
        return response.Response(result ,status=status.HTTP_200_OK)
