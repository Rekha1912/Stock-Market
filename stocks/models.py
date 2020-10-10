from django.db import models

class Userstock(models.Model):
    stockname = models.CharField(max_length=20)
    latestprice = models.IntegerField()
    quantity = models.IntegerField()
    value = models.IntegerField()
    STOCK_ACTION = [
        ('buy', 'BUY'),
        ('sell', 'SELL'),
    ]
    action = models.CharField(
        max_length=30,
        choices=STOCK_ACTION,
        default='BUY',
    )
      
    def __str__(self):
        return self.stockname