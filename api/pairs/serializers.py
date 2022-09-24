from rest_framework import serializers

from api.pairs.models import Pair


class PairListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = ['id', 'asset_to', 'asset_from', 'ratio']


class PairDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pair
        fields = '__all__'
