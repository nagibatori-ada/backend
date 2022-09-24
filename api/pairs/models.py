from django.db import models

from api.assets.models import Asset


class Pair(models.Model):
    class Meta:
        verbose_name = 'Пара'
        verbose_name_plural = 'Пары'

    description = models.TextField(
        verbose_name='Описание пары',
        null=True,
        blank=True
    )

    asset_from = models.ForeignKey(to=Asset, related_name='pairs_asset_from', on_delete=models.CASCADE)
    asset_to = models.ForeignKey(to=Asset, related_name='pairs_asset_to', on_delete=models.CASCADE)

    ratio = models.DecimalField(max_digits=15, decimal_places=10)  # todo: переделать в логику

    def __str__(self) -> str:
        return f'{self.asset_from} - {self.asset_to}'
