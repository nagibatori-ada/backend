from django.urls import path

from api.transactions.views import TransactionListView, TransactionDetailView


urlpatterns = [
    path('list/', TransactionListView.as_view()),
    path('detail/<int:pk>/', TransactionDetailView.as_view()),
]
