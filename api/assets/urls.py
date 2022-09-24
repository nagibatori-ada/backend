from django.urls import path

from api.assets.views import AssetListView, AssetDetailView

urlpatterns = [
    path('list/', AssetListView.as_view()),
    path('detail/<int:pk>/', AssetDetailView.as_view()),
]
