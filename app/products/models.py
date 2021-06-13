from django.db import models
from django.utils.translation import ugettext_lazy as _


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('name'))
    price = models.IntegerField(verbose_name=_('price'))

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')
