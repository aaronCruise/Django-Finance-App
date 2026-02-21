# Defines a model to store stock price data
from django.db import models

MAX_DIGITS = 100
DECIMAL_PLACES = 5

class Stock(models.Model):
    ticker = models.CharField(max_length=10)
    date = models.DateField()
    dayOpen = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES, null=True, blank=True)
    dayHigh = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES, null=True, blank=True)
    dayLow = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES, null=True, blank=True)
    dayClose = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES, null=True, blank=True)
    dayVolume = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.ticker
