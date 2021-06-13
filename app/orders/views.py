from rest_framework import viewsets

from . import models, serializers


class OrderView(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
