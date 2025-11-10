# Lists all the S3 buckets in your AWS account.
import boto3

s3 = boto3.client('s3')
response = s3.list_buckets()  # full response dict

# Access the list of buckets
buckets = response['Buckets']

# Print bucket names
for bucket in buckets:
  print(bucket['Name'])