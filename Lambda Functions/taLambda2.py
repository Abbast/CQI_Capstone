import json
import boto3

# Create a glue client
client = boto3.client('glue')
glueJobName = 'ta-g2'

# Define the lambda function
def lambda_handler(event, context):
    
    response = client.start_job_run(JobName = glueJobName)
    print(json.dumps(response, indent = 4))
 
