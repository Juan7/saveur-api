from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import api

app_name = 'accounts'

router = DefaultRouter()
router.register('users', api.UserViewSet, base_name='api_users')

apipatterns = router.urls + []

urlpatterns = [
    path('api/', include(apipatterns)),
]
