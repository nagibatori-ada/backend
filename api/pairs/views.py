from rest_framework import generics

from api.pairs.models import Pair
from api.pairs.serializers import PairListSerializer, PairDetailSerializer


class PairListView(generics.ListCreateAPIView):
    queryset = Pair.objects.all()
    serializer_class = PairListSerializer


class PairDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pair.objects.all()
    serializer_class = PairDetailSerializer
