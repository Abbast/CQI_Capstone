import boto3

# Create a boto3 session and client
session = boto3.Session(region_name = 'us-east-1')
s3client = session.client('s3')

# Create our four buckets in AWS
s3client.create_bucket(Bucket = 'ta-s3-staging')
s3client.create_bucket(Bucket = 'ta-s3-1')
s3client.create_bucket(Bucket = 'ta-s3-2')