from rest_framework import viewsets

from . import models, serializers


class ProductView(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
