from django.core.management.base import BaseCommand, CommandError
import boto3

from django.conf import (
    settings,
)

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('Uploading to S3')

        client = boto3.client(
        's3',
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        region_name=settings.AWS_S3_REGION_NAME
        )

        s3_upload = client.put_object(
            Bucket=settings.AWS_STORAGE_BUCKET_NAME,
            Body=b'This is a byte file',
            Key='TestFile.txt'
        )

        s3_status = client.list_objects(
            Bucket=settings.AWS_STORAGE_BUCKET_NAME
        )

        print(s3_status)
