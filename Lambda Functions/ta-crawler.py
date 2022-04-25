import json
import boto3

# Create a glue client
client = boto3.client('glue')
crawlerName = 'ta-crawler'

def lambda_handler(event, context):
    
    print('-----------------------------------')
    response = client.start_crawler(Name = crawlerName)
    print(json.dumps(response, indent = 4))
