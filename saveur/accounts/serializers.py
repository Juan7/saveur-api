from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.utils import translation
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """User model serializers."""

    class Meta:
        """User serializer meta data."""

        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': False
            }
        }

    def validate_password(self, value):
        password_validation.validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        instance = super().update(instance, validated_data)

        if password:
            instance.set_password(password)
            instance.save()

        return instance
