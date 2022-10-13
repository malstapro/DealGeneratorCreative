from django.db import models


class AdminPanel(models.Model):
    deal = models.IntegerField(default=200)
    profit_all = models.FloatField(default=0)
    profit_risk = models.FloatField(default=0)
    profit_balance = models.FloatField(default=0)

class Deal(models.Model):
    crypto = models.CharField(max_length=100,verbose_name='Название Крипты')
    date = models.DateTimeField(auto_now_add=True)
    entry_price = models.FloatField()
    sell_price = models.FloatField()
    profit = models.FloatField()
    event = models.CharField(max_length=100, default='Growth')
    exchange = models.CharField(max_length=100)
    type = models.CharField(max_length=100, default=None, blank=True, null=True)
