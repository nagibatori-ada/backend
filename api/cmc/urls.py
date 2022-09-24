from django.urls import path

from api.cmc.views import CoinMarketCupView

urlpatterns = [path('', CoinMarketCupView.as_view())]
