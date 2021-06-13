from django.db import models
from django.utils.translation import ugettext_lazy as _


class Order(models.Model):
    customer_name = models.CharField(max_length=256, verbose_name=_('customer name'))
    customer_city = models.CharField(max_length=256, verbose_name=_('customer city'))
    customer_country = models.CharField(max_length=256, verbose_name=_('customer country'))
    products = models.ManyToManyField('products.Product', verbose_name=_('products'), related_name='orders')
    longitude = models.DecimalField(max_digits=8, decimal_places=3)
    latitude = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
