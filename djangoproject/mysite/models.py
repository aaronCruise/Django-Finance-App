# Defines a model to store stock price data
from django.db import models

MAX_DIGITS = 10
DECIMAL_PLACES = 5

class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    date = models.DateField()
    dayOpen = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    dayHigh = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    dayLow = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    dayClose = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)
    dayVolume = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES)

    def __str__(self):
        return self.ticker
