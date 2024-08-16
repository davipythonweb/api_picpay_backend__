from ninja import Router
from .schemas import TransactionSchema
from django.shortcuts import get_object_or_404

from users.models import User

from rolepermissions.checkers import has_permission

from django.db import transaction as django_transaction


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
    

    # GERENCIADOR DE CONTEXTO->Atomicidade=>tudo será salvo em uma camada intermediaria(qualquer excessão será dado um rowback de tudo que foi feito)
    with django_transaction.atomic():
        payer.pay(transaction.amount)
        payee.receive(transaction.amount)

        table_transaction = transaction(
            amount=transaction.amount,
            payer_id=transaction.payer,
            payee_id=transaction.payee
        )
        payer.save()
        payee.save()
        table_transaction.save()
    
    return 200, {'transaction_id': 1}


#  tempo do video  1:16:14