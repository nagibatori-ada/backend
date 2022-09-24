from rest_framework import serializers

from api.assets.serializers import AssetListSerializer, AssetDetailSerializer
from api.transactions.models import Transaction


class TransactionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'status', 'quantity', 'gas_used', 'asset_from', 'asset_to']

    asset_to = AssetListSerializer()
    asset_from = AssetListSerializer()


class TransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

    asset_to = AssetDetailSerializer()
    asset_from = AssetDetailSerializer()
