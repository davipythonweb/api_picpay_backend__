from ninja import Router
from .schemas import TransactionSchema
from django.shortcuts import get_object_or_404

from users.models import User

from rolepermissions.checkers import has_permission


payments_router = Router()

@payments_router.post('/', response={200: dict, 400:dict, 403: dict})
def transaction(request, transaction: TransactionSchema):
    payer = get_object_or_404(User, id=transaction.payer)
    payee = get_object_or_404(User, id=transaction.payee)


    if payer.amount < transaction.amount:
        return 400, {'error': 'Saldo Insuficiente.'}
    

    if not has_permission(payer, 'make_transfer'):
        return 403, {'error': 'Voce não possui permissao para realizar tranferência.'}
    
    if not has_permission(payee, 'receive_tranfer' ):
        return 403, {'error': 'O usuario não pode receber tranferências.'}
    return 200, {'transaction_id': 1}


#  tempo do video  1:16:14