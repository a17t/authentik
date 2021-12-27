"""Apply flow from commandline"""
from django.core.management.base import BaseCommand, no_translations

from authentik.blueprints.v1.importer import Importer


class Command(BaseCommand):  # pragma: no cover
    """Apply flow from commandline"""

    @no_translations
    def handle(self, *args, **options):
        """Apply all flows in order, abort when one fails to import"""
        for flow_path in options.get("flows", []):
            with open(flow_path, "r", encoding="utf8") as flow_file:
                importer = Importer(flow_file.read())
                valid = importer.validate()
                if not valid:
                    raise ValueError("Flow invalid")
                importer.apply()

    def add_arguments(self, parser):
        parser.add_argument("flows", nargs="+", type=str)
