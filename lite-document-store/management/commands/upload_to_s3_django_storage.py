from django.core.management.base import BaseCommand, CommandError
import boto3

from django.conf import (
    settings,
)

from django.core.files.storage import default_storage

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Uploading to S3')

        file = default_storage.open('storage_test', 'w')
        file.write('storage contents')
        file.close()

        
