""" Create django management command to download finance data to csv file."""
from django.core.management.base import BaseCommand, CommandError
from pipeline.downloader import download_data, save_to_csv

class Command(BaseCommand):
    """Represents the python manage.py download command."""
    help = 'Download Yahoo Finance data to csv file'

    def add_arguments(self, parser):
        parser.add_argument(
            "ticker",
            type=str,
            help="Ticker symbol of data"
        )

    def handle(self, *args, **options):
        df = download_data(options["ticker"])
        save_to_csv(df)
