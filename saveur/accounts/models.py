from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """An extension of user model."""

    MALE = 1
    FEMALE = 2
    GENERE_CHOICES = (
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    genere = models.IntegerField(choices=GENERE_CHOICES, default=MALE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.username} profile'
