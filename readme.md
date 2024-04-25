## serverlessImageAnalysis

This Lambda function is triggered by a S3 upload. The bucket name and object key is parsed from the event parameter. 
Rekogition uses the name and key to fetch the image from the S3 bucket. Rekognition generates labels from the image and the confidence score for each label.
The image and labels are stored in dynamoDB.

## Goals

- AWS Lambda function triggered with Amazon S3 upload
- Amazon Rekognition for image analysis
- DynamoDB to store processed images

### Lambda

- boto3 sdk for python
- s3 trigger on upload

### Rekognition

- [aws documentation](https://docs.aws.amazon.com/rekognition/latest/dg/images-s3.html) for rekognition fetching s3 images
- must be the same region as s3 or cannot access s3
- confidence in labels must be stored as an int or a string

### Dynamodb

- cannot store floats. Decimal library is used to convert float to int for storage
- alternatively people store floats as strings in dynamodb