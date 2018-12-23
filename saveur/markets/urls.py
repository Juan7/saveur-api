from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import api

app_name = 'markets'

router = DefaultRouter()
router.register('markets', api.MarketViewSet, base_name='api_market')
router.register('merchants', api.MerchantViewSet, base_name='api_merchant')

apipatterns = router.urls + []

urlpatterns = [
    path('api/', include(apipatterns)),
]
