from rest_framework import serializers


class CoinMarketCapSerializer(serializers.Serializer):

    # def update(self, instance, validated_data):
    #     pass
    #
    # def create(self, validated_data):
    #     pass

    ticker = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=100)
    volume = serializers.DecimalField(max_digits=100, decimal_places=0)
    volume_24h = serializers.DecimalField(max_digits=100, decimal_places=0)
    stakeholders = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=100, decimal_places=0)
