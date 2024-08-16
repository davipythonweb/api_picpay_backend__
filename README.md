# Desafio_Backend_PICPAY/\/\/\/>Django + Django_Ninja


- API de tranferencia Bancaria com gerenciador de contexto para verificar transação

- dois usuarios: people and company

- people=> faz e recebe tranfarências


- company=> só recebe tranferências

- enviando uma notificação , apos as transaçoes com=> django-q
- para rodar o worker com o CLUSTER  simulado do django-q =>
`python3 manage.py qcluster`

- error ao usar o django-q==1.3.9
"""
from django.utils import baseconv
ImportError: cannot import name 'baseconv' from 'django.utils' (/home/davi/Música/api_picpay_backend__/venv/lib/python3.10/site-packages/django/utils/__init__.py)
"""


-BIBLIOTECA HUEY com banco separado para notificações.
- comando para rodar o WORKER do huey para  simulação de um CLUSTER de envio de notificação Assincrona no terminal=>
`huey_consumer.py payments.tasks.HUEY`


- desafio PIcPay url do git `https://github.com/PicPay/picpay-desafio-backend`



- config-admin-django
`adm-super`
`Admin#45`
`adm@contato.com`


- Corpo da requisição para enviar no teste de transação  da api
"""
{
    "amount": 5,
    "payer_id": 8,
    "payee_id": 7
}

"""