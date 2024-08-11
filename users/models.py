from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal


class User(AbstractUser):
    cpf = models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    amount = models.DecimalField(max_digits=15, decimal_places=2)

    # sobrescrever o salvamento do cpf para nao ter pontos nem virgulas .
    def save(self, *args, **kwargs):
        self.cpf = self.cpf.replace('.', '').replace('-', '')
        super(User, self).save(*args, **kwargs)

    def pay(self, value: Decimal):
        if not isinstance(value, Decimal):
            raise TypeError('Ops! Valor deve ser em decimal')
        

        # Trabalhando com atomicidade(só sera salva quando todas as auteraçoes forem feitas) antes, sera salvo em uma camada intermediaria .
        self.amount -= value

    def receive(self, value: Decimal):
        if not isinstance(value, Decimal):
            raise TypeError('Ops! Valor deve ser em decimal.')
        
        self.amount += value
