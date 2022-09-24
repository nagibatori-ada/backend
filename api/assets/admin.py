from django.contrib import admin

# Register your models here.
from api.assets.models import Asset


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'ticker',
    )
