from HellaSwap.celery import app
import time

from api.assets.models import Asset
from api.transactions.models import Transaction


@app.task
def send_transaction_and_wait_for_ending(gas_used: int, transaction_id: str):
    try:
        transaction = Transaction.objects.get(transaction_id=transaction_id)
    except Transaction.DoesNotExist:
        return

    # while True:
    time.sleep(10)  # FIXME: wait for transaction end
    transaction.update_status(status=Transaction.StatusEnum.done, gas_used=gas_used)