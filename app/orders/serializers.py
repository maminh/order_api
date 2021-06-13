from rest_framework import serializers

from . import models


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ('id', 'customer_name', 'customer_city', 'customer_country', 'products', 'longitude', 'latitude',)
