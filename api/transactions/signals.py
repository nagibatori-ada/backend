from django.db.models import signals
from django.dispatch import receiver

from api.tasks import send_transaction_and_wait_for_ending
from api.transactions.models import Transaction


@receiver(signals.post_save, sender=Transaction)
def post_save_transaction(sender, instance, created, **kwargs):
    if created:
        send_transaction_and_wait_for_ending.delay(
            model_id=instance.id,
            gas_used=22222228,
        )
