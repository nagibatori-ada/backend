from rest_framework.response import Response
from rest_framework.views import APIView


class CoinMarketCupView(APIView):

    def get(self, request):
        data = {
            'GINN':
                {
                    'volume': 1231231222222288888888828828282888282341274175249184671784126784712684,
                    'volume_24_hours': 12421442147126741412641246127451264124127847124571247127481268412,
                    'stake_holders': 4172864781274781244712564124621487124528174721467126457215421946,
                    'price': 124,
                },
            'ethereum':
                {
                    'volume': '12312312222222888888888288282828882823',
                    'volume_24_hours': '12312',
                    'stake_holders': '4172864781274781246',
                },
            'bitcoin':
                {
                    'volume': '10000',
                    'volume_24_hours': '12312',
                    'stake_holders': '4172864781274781246',
                }
        }
        return Response(data, status=200)
