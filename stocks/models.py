from django.db import models

class Userstock(models.Model):
    username = models.CharField(max_length=30)
    stockname = models.CharField(max_length=20)
    lastprice = models.FloatField()
    quantity = models.IntegerField()
    cashvalue = models.FloatField()

    STOCK_ACTION = [
        ('buy', 'BUY'),
        ('sell', 'SELL'),
    ]
    action = models.CharField(
        max_length=10,
        choices = STOCK_ACTION,
    )

    def __str__(self):
        return self.stockname