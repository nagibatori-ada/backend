from random import randint

from django.db import models
from django.db.models import Sum

from datetime import datetime, timedelta


class Asset(models.Model):
    class Meta:
        verbose_name = 'Токен'
        verbose_name_plural = 'Токены'

    name = models.CharField(verbose_name='Название', max_length=100)
    ticker = models.CharField(verbose_name='Тикер', max_length=10)
    description = models.TextField(
        verbose_name='Описание токена', null=True, blank=True
    )
    asset_id = models.CharField(verbose_name='Айди токена', max_length=255)

    def __str__(self) -> str:
        return str(self.ticker)

    @property
    def volume_24h(self) -> int:
        from api.transactions.models import Transaction

        last24h = datetime.now() - timedelta(hours=24)
        queryset = Transaction.objects.filter(
            asset_from=self, timestamp__gte=last24h
        ) | Transaction.objects.filter(asset_to=self, timestamp__gte=last24h)
        if not queryset.exists():
            return 0
        # queryset = queryset.aggregate(Sum('quantity'))['quantity__sum']
        return randint(50, 500)
