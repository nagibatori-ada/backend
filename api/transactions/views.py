from rest_framework import generics

from api.transactions.models import Transaction
from api.transactions.serializers import TransactionListSerializer, TransactionDetailSerializer


class TransactionListView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionListSerializer


class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionDetailSerializer
