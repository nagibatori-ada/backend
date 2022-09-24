from django.contrib import admin

# Register your models here.
from api.transactions.models import Transaction


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('status', 'asset_from', 'asset_to', 'timestamp')
