from HellaSwap.celery import app
import time

from api.transactions.models import Transaction


@app.task
def send_transaction_and_wait_for_ending(fee_used: int, model_id: int):
    try:
        transaction = Transaction.objects.get(id=model_id)
    except Transaction.DoesNotExist:
        return

    # while True:
    time.sleep(10)  # FIXME: wait for transaction end
    transaction.update_status(status=Transaction.StatusEnum.done, fee_used=fee_used)
