from rest_framework import serializers

from api.assets.models import Asset
from api.assets.serializers import AssetDetailSerializer, AssetListSerializer
from api.pairs.models import Pair


class PairListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = ['id', 'asset_a', 'asset_b', 'weight_a', 'weight_b', 'contract_id']

    asset_a = AssetListSerializer()
    asset_b = AssetListSerializer()


class PairDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = '__all__'

    asset_a = AssetDetailSerializer()
    asset_b = AssetDetailSerializer()


class PairCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = '__all__'
