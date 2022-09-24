from django.urls import path

from api.assets.views import AssetListView, AssetDetailView

urlpatterns = [
    path('all/', AssetListView.as_view()),
    path('<int:pk>/', AssetDetailView.as_view()),
]
