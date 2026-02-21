"""Create a django management command to analyze csv file data."""
from django.core.management.base import BaseCommand, CommandError
from pipeline.analyzer import analyze_data

class Command(BaseCommand):
    """Represents the python manage.py analyze command."""
    help = 'Load csv data and inspect/analyze data'

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            type=str,
            help="Path of csv file to analyze"
        )

    def handle(self, *args, **options):
        analyze_data(options["csv_file"])
