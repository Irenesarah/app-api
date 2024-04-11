"""
Django command to wait for the databases to be available

"""
from typing import Any # noqa
import time
from psycopg2 import OperationalError as Pscycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for a database"""

    def handle(self, *args, **options):
        self.stdout.write('waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Pscycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable,waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
