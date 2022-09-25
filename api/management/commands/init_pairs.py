import string

from django.db import utils
from django.core.management import BaseCommand

from random import randint, choices

from api.assets.models import Asset
from api.pairs.models import Pair


class Command(BaseCommand):
    def handle(self, *args, **options):
        def random_string(n: int) -> str:
            return ''.join(choices(string.ascii_uppercase + string.digits, k=n))

        try:
            print(Asset.objects.all())
            for asset_1 in Asset.objects.all():
                for asset_2 in Asset.objects.all():
                    print(asset_1, asset_1)
                    weight_a = randint(1, 100)
                    weight_b = randint(1, 100)

                    if asset_1 != asset_2:
                        if not Pair.objects.filter(
                            asset_a=asset_1, asset_b=asset_2
                        ).exists():
                            Pair.objects.create(
                                description=random_string(25),
                                asset_a=asset_1,
                                asset_b=asset_2,
                                weight_a=weight_a,
                                weight_b=weight_b,
                                contract_id='3t1eC1rzmmwseBxXqyfJf3QLupFRSv39CSSQQ9eG8eB4',
                            )
                        if not Pair.objects.filter(
                            asset_a=asset_2, asset_b=asset_1
                        ).exists():
                            Pair.objects.create(
                                description=random_string(25),
                                asset_a=asset_2,
                                asset_b=asset_1,
                                weight_a=weight_b,
                                weight_b=weight_a,
                                contract_id='3t1eC1rzmmwseBxXqyfJf3QLupFRSv39CSSQQ9eG8eB4',
                            )
        except utils.OperationalError as e:
            self.stdout.write(self.style.ERROR('Exception: %s' % e))
