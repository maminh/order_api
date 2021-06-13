from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from products.models import Product

from . import models


class ProductInline(admin.StackedInline):
    model = Product
    fields = ('id', 'name', 'price')
    extra = 0
    show_change_link = True


class OrderResource(resources.ModelResource):
    class Meta:
        model = models.Order
        fields = ('id', 'customer_name', 'customer_city', 'customer_country', 'longitude', 'latitude',)
        export_order = fields


@admin.register(models.Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('id', 'customer_name', 'customer_city', 'customer_country', 'longitude', 'latitude',)
    fields = ('id', 'customer_name', 'customer_city', 'customer_country', 'products', 'longitude', 'latitude',)
    resource_class = OrderResource
