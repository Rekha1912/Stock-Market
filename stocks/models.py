from django.db import models

class Userstock(models.Model):
    username = models.CharField(max_length=30)
    stockname = models.CharField(max_length=20)
    lastprice = models.FloatField()
    quantity = models.IntegerField()

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

class Cash(models.Model):
    username = models.CharField(max_length=30, unique=True)
    cashvalue = models.FloatField(default=10000)

    def __str__(self):
        return self.username

class StockQuantity(models.Model):
    username = models.CharField(max_length=30)
    stockname = models.CharField(max_length=20)
    quantity = models.IntegerField(null=True,default=0)

    class Meta:
        unique_together = ('username', 'stockname')

    def __str__(self):
        return self.username                  