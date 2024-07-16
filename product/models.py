from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()

    def __str__(self) -> str:
        return self.name
    
    # para mostrar o preço formatado com duas casas decimais
    def exibe_price(self):
        return "{:.2f}".format(self.price)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    status = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.email