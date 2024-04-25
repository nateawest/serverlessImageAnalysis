import boto3
from decimal import Decimal
from dotenv import load_dotenv
import os

def test_sdk():
    # testing out boto3 sdk with simple list buckets function
    # S3 service client
    s3 = boto3.client('s3')

    # List all buckets
    buckets = s3.list_buckets()
    for bucket in buckets['Buckets']:
        print(bucket['Name'])

def rekognition_test():
    response = rekognition_client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': 'bucketsoc',
                'Name': 'IMG_0004.JPG'
            }
        },
        # Number of items rekognition will identify in image.
        MaxLabels = 3,
        # Confidence rekognition has in the identified label
        MinConfidence = 75
    )

    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table('ImageTags')

    # process image, had to use decimal library to convert float to int because dynamodb does not store floats. Alt could store float as a string
    labels = [{'Label': label['Name'], 'Confidence': Decimal(str(round(label['Confidence'], 2)))} for label in response['Labels']]
    table.put_item(
        Item={
            'image_id': 'IMG_0004.JPG',
            'labels': labels
        }
    )

load_dotenv()  # load environment variables from .env file
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

test_sdk()

# must be same region as S3 bucket
rekognition_client = boto3.client('rekognition', region_name='us-east-2')
rekognition_test()

