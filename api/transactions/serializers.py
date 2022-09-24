from rest_framework import serializers

from api.transactions.models import Transaction


class TransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'status', 'coin_amount', 'gas_used', 'asset_from', 'asset_to']


class TransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
