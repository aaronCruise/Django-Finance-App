"""Define a Django Model to represent historical stock data."""
from django.db import models

MAX_TICKER_LEN = 10
MAX_DIGITS = 100
DECIMAL_PLACES = 5

class Stock(models.Model):
    """
    Represents a single day of stock market data.
    Each record corresponds to one trading day.
    """
    ticker = models.CharField(max_length=MAX_TICKER_LEN)
    date = models.DateField()
    dayOpen = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES, null=True, blank=True)
    dayHigh = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES, null=True, blank=True)
    dayLow = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES, null=True, blank=True)
    dayClose = models.DecimalField(max_digits=MAX_DIGITS, decimal_places=DECIMAL_PLACES, null=True, blank=True)
    dayVolume = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        """Return a string representation of the Stock model."""
        return self.ticker
