# Desafio_Backend_PICPAY/\/\/\/>Django + Django_Ninja

`url do Desafio PiC-PaY`
- [https://github.com/PicPay/picpay-desafio-backend]


## API de tranferencia Bancaria com gerenciador de contexto para verificar transações

>   Dois usuarios=> people and company: :heavy_check_mark:


> People=> faz e recebe tranfarências:   :heavy_check_mark:

> Company=> só recebe tranferências:  :heavy_check_mark:

> BIBLIOTECA HUEY com banco separado para processamento de fila de notificações :heavy_check_mark:


- enviando uma notificação , apos as transaçoes com=> django-q :warning:
- para rodar o worker com o CLUSTER  simulado do django-q =>
`python3 manage.py qcluster`

- error ao usar o django-q==1.3.9
"""
from django.utils import baseconv
ImportError: cannot import name 'baseconv' from 'django.utils' (/home/davi/Música/api_picpay_backend__/venv/lib/python3.10/site-packages/django/utils/__init__.py)
"""


`Implementado`
- comando para rodar o WORKER do huey para  simulação de um CLUSTER de envio de notificação Assincrona no terminal=> :heavy_check_mark:
`huey_consumer.py payments.tasks.HUEY`

- comando para acrescentar mais threads --workers= >
`huey_consumer.py payments.tasks.HUEY --workers=4`



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
