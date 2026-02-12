# Create django management command to import csv dat into database
from django.core.management.base import BaseCommand, CommandError
from mysite.models import Stock
import pandas as pd

TICKER = "VT" # hard coded for now

class Command(BaseCommand):
    help = 'Imports CSV data into the Django ORM'

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file", 
            type=str,
            help="Name of the .csv file"
        )

    def handle(self, *args, **options):
        input_file = options["csv_file"]
        dataFrame = pd.read_csv(input_file, index_col=False)

        stocks = []
        for _, row in dataFrame.iterrows():
            stocks.append(
                    Stock(
                    ticker=TICKER,
                    date=pd.to_datetime(row["Date"]).date(),
                    dayOpen=row["Open"],
                    dayHigh=row["High"],
                    dayLow=row["Low"],
                    dayClose=row["Close"],
                    dayVolume=row["Volume"]
                    )
        )
        Stock.objects.bulk_create(stocks)
        self.stdout.write(f"Successfully imported {input_file} into the Django ORM.") 
