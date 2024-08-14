from ninja import Router
from .schemas import TransactionSchema
from django.shortcuts import get_object_or_404

from users.models import User

payments_router = Router()

@payments_router.post('/', response={200: dict, 400:dict})
def transaction(request, transaction: TransactionSchema):
    payer = get_object_or_404(User, id=transaction.payer)
    payee = get_object_or_404(User, id=transaction.payee)


    if payer.amount < transaction.amount:
        return 400, {'error': 'Saldo Insuficiente.'}

    # print(transaction.dict())
    return 200, {'transaction_id': 1}


#  tempo do video 1:13:18