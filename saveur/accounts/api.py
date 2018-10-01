import django_filters

from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, views, viewsets, response, mixins, status

from utils import pagination

from . import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.UserSerializer

    pagination_class = pagination.StandardResultsSetPagination
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter)
    queryset = User.objects.all()
    ordering = ('-pk')
    filter_fields = {}

    def update(self, request, pk=None):
        if (request.data.get('id')
                and request.data.get('password')
                and request.data.get('password') != request.data.get('password2')):
            result = {
                'password': 'Los passwords deben coincidir',
                'password2': 'Los passwords deben coincidir'}
            return response.Response(result ,status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, pk)

    def perform_create(self, serializer):
        user = serializer.save()
        user.profile.save()
