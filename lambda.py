import boto3
from decimal import Decimal
from dotenv import load_dotenv
import logging
import os
import sys


def lambda_handler(event, context):
    # grab bucket name from the trigger event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    # grab s3 object key *file-name
    key = event['records'][0]['s3']['object']['key']

    # call rekognition method with bucket and image name
    rekognition_method(bucket_name, key)

def test_sdk():
    # testing out boto3 sdk with simple list buckets function
    # S3 service client
    s3 = boto3.client('s3')

    # List all buckets
    buckets = s3.list_buckets()
    for bucket in buckets['Buckets']:
        print(bucket['Name'])

def rekognition_method(bucket_name, key):carl


    # Creat rekognition client. must be same region as S3 bucket
    rekognition_client = boto3.client('rekognition', region_name='us-east-2')
    response = rekognition_client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket_name,
                'Name': key
            }
        },
        # Number of items rekognition will identify in image.
        MaxLabels = 3,
        # Confidence rekognition has in the identified label
        MinConfidence = 75
    )

    # create dynamodb client
    dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    table = dynamodb.Table('ImageTags')

    # process image, had to use decimal library to convert float to int because dynamodb does not store floats. Alt could store float as a string
    labels = [{'Label': label['Name'], 'Confidence': Decimal(str(round(label['Confidence'], 2)))} for label in response['Labels']]
    dynamo_response = table.put_item(
        Item={
            'image_id': key,
            'labels': labels
        }
    )
  

load_dotenv()  # load environment variables from .env file
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")
IMAGE_KEY = os.getenv("IMAGE_KEY")

# test_sdk()
rekognition_method(BUCKET_NAME, IMAGE_KEY)

