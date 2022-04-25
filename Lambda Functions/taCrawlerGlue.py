# Set up logging
import json
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Import Boto3 for AWS Glue
import boto3
client = boto3.client('glue')

# Variables for the Job
glueJobName = 'ta-glue2'

# Define the Lambda function
def lambda_handler(event, context):
    logger.info('## INITIATED BY EVENT: ')
    logger.info(event['detail'])
    response = client.start_job_run(JobName = glueJobName)
    
    logger.info('## STARTED GLUE JOB: ' + glueJobName)
    logger.info('## GLUE JOB RUN ID: ' + response['JobRunId'])
    return response
