from dotenv import dotenv_values  
import boto3  
import datetime 
import pandas as pd

config = dotenv_values(".env")  
  
s3 = boto3.client('s3',     
    endpoint_url='https://eu2.contabostorage.com',     
    aws_access_key_id=config['AWS_ACCESS_KEY_ID'],     
    aws_secret_access_key=config['AWS_SECRET_ACCESS_KEY']  
)    
    
bucket_name = 'home-credit-credit-risk-model-stability'    
  
# Download tables.txt from the bucket  
s3.download_file(bucket_name, 'tables.txt', 'tables.txt')  
  
# Read tables.txt  
with open('tables.txt', 'r') as file:  
    tables = [line.strip() for line in file]  
  
# Download all files listed in tables.txt  
df_list = []  
for table in tables:  
    print(f'Downloading {table} from {bucket_name}...')  
    local_filename = table.replace(':', '_')  
    s3.download_file(bucket_name, table, "./downloaded/"+local_filename)  
    datetime_str = table.split('home-credit-credit-risk-model-stability-publicleaderboard-')[-1].rstrip('.csv')  
    dt = datetime.datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S")  
    df = pd.read_csv("./downloaded/"+local_filename)  
    df['DownloadTime'] = dt.replace(minute=0, second=0)   
    df_list.append(df)  
  
df_concat = pd.concat(df_list, ignore_index=True)  
df_concat.to_csv("./downloaded/public_leaderboard.csv")

print("Uploading leaderboard")
bucket_name = 'home-credit-credit-risk-model-stability-public-leaderboard'  
s3.upload_file("./downloaded/public_leaderboard.csv", bucket_name, "public_leaderboard.csv") 