from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path(
        'docs/',
        get_swagger_view(
            title='NAGIBATORI ADA API',
            url='/',
        ),
    ),
    path('transaction/', include('api.transactions.urls')),
    path('trading/pairs/', include('api.pairs.urls')),
    path('trading/assets/', include('api.assets.urls')),
    path('cmc/', include('api.cmc.urls')),
]
