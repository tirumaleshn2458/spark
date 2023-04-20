from pyspark import boto3
print('Currently the boto3 integration for s3 service')
region_name=input('Enter the region name: ')
aws_access_key_id=input('Enter the aws_access_key_id: ')
aws_secret_access_key=input('Enter the aws_secret_access_key: ')
connection=None
try:
    s3_client = boto3.resource(service_name='s3', region_name=region_name,
                                   aws_access_key_id=aws_access_key_id,
                                   aws_secret_access_key=aws_secret_access_key)
    print('Connected')
    connection='Success'
except:
    s3_client = boto3.resource(service_name='s3', region_name=region_name,
                                   aws_access_key_id=aws_access_key_id,
                                   aws_secret_access_key=aws_secret_access_key)

if connection=='Success':
    bucket_name=input('Enter the bucket name: ')
    file_path=input('Enter the file path to upload the file: ')
    name_file=input('Enter the name you want the file to be named: ')
    result=s3_client.Bucket(bucket_name).upload_file(file_path,name_file)
    if result==None:
        print('Uploaded successfully')
