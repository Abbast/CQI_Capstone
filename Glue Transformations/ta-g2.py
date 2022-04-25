import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

import boto3
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import pandas as pd
from io import StringIO

# Instantiate a connection to an s3 bucket
s3 = boto3.resource('s3')
bucket = s3.Bucket('ta-s3-1')

# Create a dictionary to read files in the s3 bucket into
dict = {}
tick = 0

# Iterate through all the objects in the bucket and obtain the body
for obj in bucket.objects.all():
    key = obj.key
    body = obj.get()['Body'].read()
    
    
    dict[tick] = body
    tick = tick + 1

# Convert files into a format that can be read into a pandas dataframe
s0 = str(dict[0], 'utf-8')
data_0 = StringIO(s0)

s1 = str(dict[1], 'utf-8')
data_1 = StringIO(s1)

s2 = str(dict[2], 'utf-8')
data_2 = StringIO(s2)

# Read files into pandas dataframes
df_0 = pd.read_csv(data_0, sep = ",", lineterminator = '\n')
df_1 = pd.read_csv(data_1, sep = ",", lineterminator = '\n')
df_2 = pd.read_csv(data_2, sep = ",", lineterminator = '\n')

def row_to_list(D):   
    bucket = []
    
    for i in range(D.shape[1]):       
        entry = D.iloc[0][i]
        bucket.append(entry)
        
    return bucket
    
# Replace the columns with the bucket
df_0.columns = row_to_list(df_0)
df_1.columns = row_to_list(df_1)
df_2.columns = row_to_list(df_2)

# Drop the first row for each table
df_0 = df_0.drop(0, axis = 'rows')
df_1 = df_1.drop(0, axis = 'rows')
df_2 = df_2.drop(0, axis = 'rows')

# Reorder the columns in df_2
df_2 = df_2[['owner', 'country_of_origin', 'company', 'altitude_mean_meters', 'region']]

# Create schemas for the dataframes

schema1 = StructType(
    [StructField("aroma", StringType(), True)\
    ,StructField("flavor", StringType(), True)\
    ,StructField("aftertaste", StringType(), True)\
    ,StructField("acidity", StringType(), True)\
    ,StructField("body", StringType(), True)\
    ,StructField("balance", StringType(), True)\
    ,StructField("uniformity", StringType(), True)\
    ,StructField("clean_cup", StringType(), True)\
    ,StructField("sweetness", StringType(), True)\
    ,StructField("moisture", StringType(), True)\
    ,StructField("category_one_defects", StringType(), True)\
    ])

schema2 = StructType(
    [StructField("species", StringType(), True)\
    ,StructField("color", StringType(), True)\
    ,StructField("processing_method", StringType(), True)
    ]
)

schema3 = StructType(
    [StructField("owner", StringType(), True)\
    ,StructField("country_of_origin", StringType(), True)\
    ,StructField("company", StringType(), True)\
    ,StructField("altitude_mean_meters", StringType(), True)\
    ,StructField("region", StringType(), True)]
)

# Read in the pandas DataFrames into PySpark dataframe objects
spark_0 = spark.createDataFrame(df_0, schema = schema1)
spark_1 = spark.createDataFrame(df_1, schema = schema2)
spark_2 = spark.createDataFrame(df_2, schema = schema3)

# Fill missing values with 'unknown'

spark_1 = spark_1.replace('NaN', 'unknown')
spark_2 = spark_2.replace('NaN', 'unknown')

# Recast datatypes in the first dataframe and the mean_altitude 
# column to floating decimals as opposed to strings

for val in spark_0.columns:

    spark_0 = spark_0.withColumn(val, spark_0[val].cast(FloatType()))

spark_2 = spark_2.withColumn("altitude_mean_meters", spark_2["altitude_mean_meters"].cast(FloatType()))

# Convert the PySpark dataframes into Pandas DataFrames
quality = spark_0.toPandas()
beans = spark_1.toPandas()
farms = spark_2.toPandas()

# Save the above DataFrames into csv files
quality.to_csv('quality.csv', index = False)
beans.to_csv('beans.csv', index = False)
farms.to_csv('farms.csv', index = False)

# Upload the files to our target s3 bucket
s3 = boto3.client('s3',
    aws_access_key_id = 'AKIA5RGT3KKYW47XSEGV',
    aws_secret_access_key = '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')
bucket = 'ta-s3-2' 
file1 = 'quality.csv'
file2 = 'beans.csv'
file3 = 'farms.csv'

s3.upload_file(file1, bucket, file1)
s3.upload_file(file2, bucket, file2)
s3.upload_file(file3, bucket, file3)

job.commit()