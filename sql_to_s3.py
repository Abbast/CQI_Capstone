# Library imports
import os
import boto3
import numpy as np
import pandas as pd
from sqlalchemy import create_engine

# Access the SQL table

# Create an engine and then open a live connection
engine = create_engine(f'postgresql://postgres:1066@localhost:5432/coffeequality')
conn = engine.connect()

# Read in the data from PostgreSQL
data = pd.read_sql("SELECT * FROM coffee", conn).drop(columns= 'index')

# Save the data to a local directory
base_path = 'C:/Users/TawfikAbbas/Documents/TalentPath/CapstoneProject/data/'
path = base_path + 'data.csv'

data.to_csv(path)

# Access the s3 bucket with boto3
s3 = boto3.resource('s3')

s3.Bucket('ta-s3-staging').upload_file(path, 'data.csv')

# Remove the file from the local directory 
os.remove(path)