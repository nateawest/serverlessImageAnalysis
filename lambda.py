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

def rekognition_test():
    response = rekognition_client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': 'bucketsoc',
                'Name': 'pic1.JPG'
            }
        },
        MaxLabels = 3,
        MinConfidence = 75
    )


load_dotenv()  # load environment variables from .env file
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

test_sdk()

rekognition_client = boto3.client('rekognition', region_name='us-east-2')
rekognition_test()

