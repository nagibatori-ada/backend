from rest_framework import serializers


class AssetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

    volume_24h = serializers.SerializerMethodField()

    @staticmethod
    def get_volume_24h(obj):
        return obj.volume_24h
