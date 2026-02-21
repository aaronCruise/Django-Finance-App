"""Create django management command to create data visualizations from csv file."""
from django.core.management.base import BaseCommand, CommandError
from pipeline.visualizer import visualize_data

class Command(BaseCommand):
    """Represents the python manage.py visualize command."""
    help = 'Plot visualizations of data'

    def add_arguments(self, parser):
        parser.add_argument(
            "csv_file",
            type=str,
            help="Path of csv file to visualize"
        )

    def handle(self, *args, **options):
        visualize_data(options["csv_file"])
