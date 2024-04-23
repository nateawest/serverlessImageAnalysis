import boto3

# Create an S3 service client
s3 = boto3.client('s3')

# List existing buckets
buckets = s3.list_buckets()
for bucket in buckets['Buckets']:
    print(bucket['Name'])