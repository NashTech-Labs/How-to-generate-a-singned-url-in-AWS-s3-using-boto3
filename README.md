## How to generate  the AWS S3 signed url using boto3.

#### Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can use Amazon S3 to store and protect any amount of data for a range of use cases, such as data lakes, websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides management features so that you can optimize, organize, and configure access to your data to meet your specific business, organizational, and compliance requirements. You can follow this [link](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-signed-urls.html) to know more.

-------------

**Files:** 
```
      s3_signed_url.py
```

## Apply the script

1. First configure the aws credentials using aws-cli.

        aws configure

2. Now, from the current directory run the following command to create signed url.

        python3 s3_signed_url.py

















