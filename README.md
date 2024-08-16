# Desafio_Backend_PICPAY/\/\/\/>Django + Django_Ninja


- API de tranferencia Bancaria com gerenciador de contexto para verificar transação

- dois usuarios: people and company

- people=> faz e recebe tranfarências

- company=> só recebe tranferências

- enviando uma notificação , apos as transaçoes com=> django-q
- para rodar o worker com o CLUSTER  simulado do django-q =>
`python3 manage.py qcluster`

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