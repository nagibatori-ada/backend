from rest_framework import generics

from api.assets.models import Asset
from api.assets.serializers import AssetListSerializer, AssetDetailSerializer


class AssetListView(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetListSerializer


class AssetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetDetailSerializer
