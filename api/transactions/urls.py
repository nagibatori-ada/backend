from django.urls import path

from api.transactions.views import TransactionListView, TransactionDetailView


urlpatterns = [
    path('all/', TransactionListView.as_view()),
    path('<int:pk>/', TransactionDetailView.as_view()),
]
