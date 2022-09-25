from django.db import models

from api.assets.models import Asset
from django.core.exceptions import ValidationError


class Pair(models.Model):
    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'

    description = models.TextField(verbose_name='Описание пары', null=True, blank=True)

    asset_a = models.ForeignKey(
        to=Asset, related_name='pairs_asset_a', on_delete=models.CASCADE
    )
    asset_b = models.ForeignKey(
        to=Asset, related_name='pairs_asset_b', on_delete=models.CASCADE
    )

    weight_a = models.DecimalField(max_digits=15, decimal_places=10)
    weight_b = models.DecimalField(max_digits=15, decimal_places=10)

    contract_id = models.CharField(max_length=255, verbose_name='Адрес контракта')

    def __str__(self) -> str:
        return f'{self.asset_a} - {self.asset_b}'

    def clean(self):
        if self.asset_a == self.asset_b:
            raise ValidationError(
                'AssetsEqualException: asset_a and asset_b should be different.'
            )
