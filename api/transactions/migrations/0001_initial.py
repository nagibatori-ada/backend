# Generated by Django 4.1.1 on 2022-09-25 07:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'status',
                    models.CharField(
                        choices=[('done', 'выполнено'), ('pend', 'ожидается')],
                        default='pend',
                        max_length=4,
                        verbose_name='Статус',
                    ),
                ),
                (
                    'timestamp',
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name='Дата'
                    ),
                ),
                (
                    'fee_used',
                    models.PositiveIntegerField(
                        blank=True, null=True, verbose_name='Комиссия'
                    ),
                ),
                (
                    'input_amount',
                    models.DecimalField(
                        decimal_places=0,
                        max_digits=100,
                        verbose_name='Объем исходного актива',
                    ),
                ),
                (
                    'output_amount',
                    models.DecimalField(
                        decimal_places=0,
                        max_digits=100,
                        verbose_name='Объем результирующего актива',
                    ),
                ),
                (
                    'target_contract_id',
                    models.CharField(max_length=255, verbose_name='Адрес контракта'),
                ),
                (
                    'transaction_id',
                    models.CharField(max_length=255, verbose_name='Айди транзакции'),
                ),
                (
                    'asset_from',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='transactions_asset_from',
                        to='assets.asset',
                    ),
                ),
                (
                    'asset_to',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='transactions_asset_to',
                        to='assets.asset',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
    ]
