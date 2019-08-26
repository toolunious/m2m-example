from django.core.management.base import BaseCommand, CommandError
from m2m.models import Characteristic

from m2m import constants

class Command(BaseCommand):
    help = 'Sync characteristics in constants.py to DB'

    def add_arguments(self, parser):
        parser.add_argument('--dry-run', action='store_true')

    def handle(self, *args, **options):
        dry_run = False
        if options['dry_run']:
            dry_run = True
            self.stdout.write(self.style.WARNING("Dry run, no changes will be done to DB"))
        changes = {}
        for characteristic_type, constant_list in constants.DB_TYPES.items():
            db_objects = Characteristic.objects.filter(type=characteristic_type)
            characteristics = dict(constant_list)
            changes[characteristic_type] = {}
            for db_characteristic in db_objects:
                try:
                    characteristics.pop(db_characteristic.constants_id)
                except KeyError:
                    # removing from DB
                    if not dry_run:
                        db_characteristic.delete()
                    changes[characteristic_type][db_characteristic.constants_id] = "DELETED"
            for constant_id, name in characteristics.items():
                if not dry_run:
                    db_characteristic = Characteristic(
                        constants_id=constant_id,
                        type=characteristic_type
                    )
                    db_characteristic.save()
                changes[characteristic_type][constant_id] = name
            self.stdout.write(self.style.SUCCESS(f"Changes: {changes}"))
