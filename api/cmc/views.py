from rest_framework.response import Response
from rest_framework.views import APIView

from api.cmc.serializers import CoinMarketCapSerializer


class CoinMarketCupView(APIView):
    def get(self, request):
        # data = {
        #     'GINN':
        #         {
        #             'volume': 1231231222222288888888828828282888282341274175249184671784126784712684,
        #             'volume_24h': 12421442147126741412641246127451264124127847124571247127481268412,
        #             'stakeholders': 4172864781274781244712564124621487124528174721467126457215421946,
        #             'price': 124,
        #         },
        #     'ethereum':
        #         {
        #             'volume': '12312312222222888888888288282828882823',
        #             'volume_24h': '12312',
        #             'stakeholders': '4172864781274781246',
        #         },
        #     'bitcoin':
        #         {
        #             'volume': '10000',
        #             'volume_24h': '12312',
        #             'stakeholders': '4172864781274781246',
        #         }
        # }
        # return Response(data, status=200)

        data = [
            {
                'ticker': 'GINN',
                'name': 'GameINN Coin',
                'volume': 12412489124,
                'volume_24h': 58151,
                'stakeholders': 4,
                'price': 10,
            },
            {
                'ticker': 'BTC',
                'name': 'Bitcoin',
                'volume': 8921412415421,
                'volume_24h': 45481512075912,
                'stakeholders': 4000000000,
                'price': 10,
            },
            {
                'ticker': 'ETH',
                'name': 'Ethereum',
                'volume': 421412,
                'volume_24h': 12412,
                'stakeholders': 1244124,
                'price': 899,
            },
        ]
        serialized = CoinMarketCapSerializer(data=data, many=True)
        serialized.is_valid(raise_exception=True)
        return Response(serialized.data)
