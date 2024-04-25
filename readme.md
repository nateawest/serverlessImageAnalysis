## Goals

- AWS Lambda function triggered with Amazon S3 upload
- Amazon Rekognition for image analysis
- DynamoDB to store processed images

### Lambda

- s3 trigger on upload
- boto3 sdk for python

### Rekognition

- [aws documentation](https://docs.aws.amazon.com/rekognition/latest/dg/images-s3.html) for rekognition fetching s3 images
- must be the same region as s3 or error msg
- confidence in labels must be stored as an int or a string

### Dynamodb

- cannot store floats. Decimal library is used to convert float to int for storage
- alternatively people store floats as strings in dynamodb