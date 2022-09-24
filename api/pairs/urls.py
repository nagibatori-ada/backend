from django.urls import path

from api.pairs.views import PairListView, PairDetailView


urlpatterns = [
    path('list/', PairListView.as_view()),
    path('detail/<int:pk>/', PairDetailView.as_view()),
]
