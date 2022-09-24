# Generated by Django 4.1.1 on 2022-09-23 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("assets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pair",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание пары"
                    ),
                ),
                ("ratio", models.DecimalField(decimal_places=10, max_digits=15)),
                (
                    "asset_from",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pairs_asset_from",
                        to="assets.asset",
                    ),
                ),
                (
                    "asset_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pairs_asset_to",
                        to="assets.asset",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пара",
                "verbose_name_plural": "Пары",
            },
        ),
    ]
