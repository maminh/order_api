from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from . import models


class ProductResource(resources.ModelResource):
    class Meta:
        model = models.Product
        fields = ('id', 'name', 'price')
        export_order = fields


@admin.register(models.Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'price')
    fields = ('name', 'price')
    resource_class = ProductResource
