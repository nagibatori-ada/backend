from rest_framework import serializers

from api.assets.models import Asset
from api.assets.serializers import AssetDetailSerializer, AssetListSerializer
from api.pairs.models import Pair


class PairListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = ['id', 'asset_to', 'asset_from', 'ratio']

    asset_to = AssetListSerializer()
    asset_from = AssetListSerializer()


class PairDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = '__all__'

    asset_to = AssetDetailSerializer()
    asset_from = AssetDetailSerializer()


class PairCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = '__all__'
