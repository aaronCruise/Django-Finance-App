# Create django management command to import csv dat into database
from django.core.management.base import BaseCommand, CommandError
from mysite.models import Stock
from pipeline.importer import import_csv_to_db
import pandas as pd

class Command(BaseCommand):
    help = 'Imports CSV data into the Django ORM'

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file", 
            type=str,
            help="Name of the .csv file"
        )
        parser.add_argument(
            "ticker",
            type=str,
            help="Ticker symbol of data"
        )

    def handle(self, *args, **options):
        Stock.objects.all().delete()
        import_csv_to_db(options["csv_file"], options["ticker"])
