# import the boto3 which will use to interact  with the aws

import boto3

REGION = input("Enter the REGION Name")
BUCKET_NAME = input("Enter the bucket name")
client_for_s3 = boto3.client("s3", region_name=REGION)

def signed_url(bucket_name, object_name):
    s3_url= client_for_s3.generate_presigned_url(ClientMethod='get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=2700)
    print(s3_url)

signed_url(BUCKET_NAME, 'techhub.txt')