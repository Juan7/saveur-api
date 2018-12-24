import os
import uuid

from decimal import Decimal

from django.contrib.auth.models import User
from django.db import models


def get_market_file_path(instance, filename):
    """Get a random filename to avoid override on server."""
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join('market/img', filename)

def get_merchant_file_path(instance, filename):
    """Get a random filename to avoid override on server."""
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join('merchant/img', filename)


def get_market_type_file_path(instance, filename):
    """Get a random filename to avoid override on server."""
    ext = filename.split('.')[-1]
    filename = '%s.%s' % (uuid.uuid4(), ext)
    return os.path.join('market_type/img', filename)


class MarketType(models.Model):
    name = models.CharField(max_length=254)
    image = models.ImageField(upload_to=get_market_type_file_path, blank=True, null=True)
    url_image = models.URLField(max_length=254, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Market(models.Model):
    name = models.CharField(max_length=254)
    short_name = models.CharField(max_length=254, blank=True, null=True)
    place = models.CharField(max_length=254, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    suggestion = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=12, default=Decimal('0.00'))
    longitude = models.DecimalField(max_digits=20, decimal_places=12, default=Decimal('0.00'))
    image = models.ImageField(upload_to=get_market_file_path, blank=True, null=True)
    url_image = models.URLField(max_length=254, blank=True, null=True)

    type = models.ForeignKey(MarketType, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class MarketSchedule(models.Model):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    DAY_CHOICES = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday')
    )

    market = models.ForeignKey(Market, on_delete=models.CASCADE, blank=True, null=True)
    day = models.IntegerField(choices=DAY_CHOICES, default=MONDAY)
    start_time = models.TimeField()
    end_time = models.TimeField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Merchant(models.Model):
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    description = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    suggestion = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=get_merchant_file_path, blank=True, null=True)
    url_image = models.URLField(max_length=254, blank=True, null=True)

    type = models.ForeignKey(MarketType, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class MerchantSchedule(models.Model):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    DAY_CHOICES = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday')
    )

    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    day = models.IntegerField(choices=DAY_CHOICES, default=MONDAY)
    start_time = models.TimeField()
    end_time = models.TimeField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MarketRate(models.Model):
    PRODUCT = 1
    PRICE = 2
    ACCESS = 3

    RATE_CHOICES = (
        (PRODUCT, 'Product'),
        (PRICE, 'Price'),
        (ACCESS, 'Access')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    type = models.IntegerField(choices=RATE_CHOICES, default=PRODUCT)
    rate = models.FloatField(default='0.00')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.market.name} - {self.rate}'


class MerchantRate(models.Model):
    PRODUCT = 1
    PRICE = 2
    ACCESS = 3

    RATE_CHOICES = (
        (PRODUCT, 'Product'),
        (PRICE, 'Price'),
        (ACCESS, 'Access')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    merchant = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    type = models.IntegerField(choices=RATE_CHOICES, default=PRODUCT)
    rate = models.FloatField(default='0.00')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.merchant.name} - {self.rate}'
