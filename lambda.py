import boto3
import os

from dotenv import load_dotenv

def test_sdk():
    # Create an S3 service client
    s3 = boto3.client('s3')

    # List existing buckets
    buckets = s3.list_buckets()
    for bucket in buckets['Buckets']:
        print(bucket['Name'])


load_dotenv()  # load environment variables from .env file
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

test_sdk()