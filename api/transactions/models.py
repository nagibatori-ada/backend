from django.db import models
from django.utils.translation import gettext_lazy as _

from api.assets.models import Asset

from django.utils import timezone


class Transaction(models.Model):
    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    class StatusEnum(models.TextChoices):
        done = 'done', _('выполнено')
        pending = 'pend', _('ожидается')

    status = models.CharField(max_length=4, choices=StatusEnum.choices, verbose_name='Статус')
    timestamp = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    gas_used = models.PositiveIntegerField(verbose_name='Использованный газ')
    amount_from = models.DecimalField(max_digits=100, decimal_places=0, verbose_name='Объем исходного актива')
    amount_to = models.DecimalField(max_digits=100, decimal_places=0, verbose_name='Объем результирующего актива')

    asset_from = models.ForeignKey(to=Asset, related_name='transactions_asset_from', on_delete=models.CASCADE)
    asset_to = models.ForeignKey(to=Asset, related_name='transactions_asset_to', on_delete=models.CASCADE)
    # transaction_id = models.CharField(max_length=255, verbose_name='Айди транзакции')
