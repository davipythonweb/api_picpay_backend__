# mostrando uma notificação simples para a transação com django-q

# def send_notification(payer, payee, amount):
#     print(f'{payer}, Acaba de enviar um pagamento para {payee}, no valor de R${amount}.')


# error ao usar o django-q==1.3.9
"""

from django.utils import baseconv
ImportError: cannot import name 'baseconv' from 'django.utils' (/home/davi/Música/api_picpay_backend__/venv/lib/python3.10/site-packages/django/utils/__init__.py)
"""



# lib para envio de notificação assincrona similar ao django-q ou Celery
from huey import SqliteHuey

# configuração
HUEY = SqliteHuey(filename='huey.db')

# decorator da task
@HUEY.task(retries=4, retry_delay=2, timeout=30)
# funçao para notificação assincrona com biblioteca huey
def send_notification(payer, payee, amount):
    print(f'{payer}, Acaba de enviar um pagamento para {payee}, no valor de R$: {amount}.')






# OBS:
""""
O Que o huey.db Armazena=>

Tarefas Enfileiradas: O banco de dados armazena as tarefas que foram enfileiradas para execução.

Estado das Tarefas: Inclui informações sobre se uma tarefa
foi processada, se falhou, ou se está pendente.

Resultados das Tarefas: Dependendo da configuração, o banco de
dados pode armazenar os resultados das tarefas executadas.

"""