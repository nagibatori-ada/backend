from django.contrib import admin

# Register your models here.
from api.pairs.models import Pair


@admin.register(Pair)
class PairAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'asset_a',
        'asset_b',
    )
