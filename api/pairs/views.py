from rest_framework import generics

from api.pairs.models import Pair
from api.pairs.serializers import (
    PairListSerializer,
    PairDetailSerializer,
    PairCreateSerializer,
)


class PairListView(generics.ListCreateAPIView):
    queryset = Pair.objects.all()
    serializer_class = PairListSerializer


class PairDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pair.objects.all()
    serializer_class = PairDetailSerializer


class PairCreateView(generics.CreateAPIView):
    serializer_class = PairCreateSerializer
