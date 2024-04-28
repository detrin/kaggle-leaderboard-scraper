from dotenv import dotenv_values
import boto3
import sys

config = dotenv_values(".env")

filename = sys.argv[1]
basename = filename.split('/')[-1]

s3 = boto3.client('s3',   
    endpoint_url='https://eu2.contabostorage.com',   
    aws_access_key_id=config['AWS_ACCESS_KEY_ID'],   
    aws_secret_access_key=config['AWS_SECRET_ACCESS_KEY']
)  
  
bucket_name = 'home-credit-credit-risk-model-stability'  

print(f'Uploading {filename} to {bucket_name}...')
s3.upload_file(filename, bucket_name, basename)

print(f'List of files in {bucket_name}:')

file_cnt = 0
with open('tables.txt', 'w') as file:    
    paginator = s3.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name)

    for page in pages:
        for obj in page['Contents']:
            if obj['Key'] != 'tables.txt':
                file.write(obj['Key'] + '\n') 
                file_cnt += 1 

print(f'{file_cnt} files uploaded')

print('Uploading tables.txt...')
s3.upload_file('tables.txt', bucket_name, 'tables.txt')  

