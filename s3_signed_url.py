# import the boto3 which will use to interact  with the aws

import boto3

AWS_REGION = input("Enter the AWS_REGION Name")
S3_BUCKET_NAME = input("Enter the bucket name")
s3_client = boto3.client("s3", region_name=AWS_REGION)

def signed_url(bucket_name, object_name):
    url = s3_client.generate_presigned_url(ClientMethod='get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=3600)
    print(url)

signed_url(S3_BUCKET_NAME, 'techhub.txt')