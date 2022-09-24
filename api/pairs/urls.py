from django.urls import path

from api.pairs.views import PairListView, PairDetailView


urlpatterns = [
    path('all/', PairListView.as_view()),
    path('<int:pk>/', PairDetailView.as_view()),
]
