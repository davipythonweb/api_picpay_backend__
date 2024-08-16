from ninja import Router
from .schemas import TransactionSchema
from django.shortcuts import get_object_or_404

from users.models import User

from rolepermissions.checkers import has_permission

from django.db import transaction as django_transaction

from .models import Transactions

import requests
from django.conf import settings



payments_router = Router()

@payments_router.post('/', response={200: dict, 400:dict, 403: dict})
def transaction(request, transaction: TransactionSchema):
    payer = get_object_or_404(User, id=transaction.payer)
    payee = get_object_or_404(User, id=transaction.payee)


    if payer.amount < transaction.amount:
        return 400, {'error': 'Saldo Insuficiente.'}
    

    if not has_permission(payer, 'make_transfer'):
        return 403, {'error': f'Usuario: {payer} não possui permissao para realizar tranferência.'}
    
    if not has_permission(payee, 'receive_tranfer' ):
        return 403, {'error': f'O usuario {payee} não pode receber tranferências.'}
    

    # GERENCIADOR DE CONTEXTO->Atomicidade=>tudo será salvo em uma camada intermediaria(qualquer excessão será dado um rowback de tudo que foi feito)
    with django_transaction.atomic():
        payer.pay(transaction.amount)
        payee.receive(transaction.amount)

        table_transaction = Transactions(
            amount=transaction.amount,
            payer_id=transaction.payer,
            payee_id=transaction.payee  
        )
        payer.save()
        payee.save()
        table_transaction.save()

        # fazendo a verificação para o mocky(simulando uma Bandeica de cartão por de autorização para a TRANSAÇÂO.  ==>exemplo (MASTERCARD) que LIBERA A TRANFERENCIA OU NÂO PARA O USUARIO)
        response = requests.get(settings.AUTHORIZE_TRANSFER_ENDPOINT).json()
        if response.get('status') != "authorized":
            raise Exception('Transação Não autorizada! Fale com sua Instituição Bancaria.')
    
    return 200, {'transaction_id': 1}

# Implementar o envio de email em fila de tarefas(celery) , com o status da transação e as informações.

#  tempo do video  1:30:22