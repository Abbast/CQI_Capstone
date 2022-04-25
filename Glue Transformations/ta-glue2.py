import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="tadata", table_name="data_csv", transformation_ctx="S3bucket_node1"
)

# Script generated for node Select Fields
SelectFields_node1650488262021 = SelectFields.apply(
    frame=S3bucket_node1,
    paths=[
        "col20",
        "col21",
        "col22",
        "col23",
        "col24",
        "col25",
        "col26",
        "col27",
        "col28",
        "col31",
        "col32",
    ],
    transformation_ctx="SelectFields_node1650488262021",
)

# Script generated for node Select Fields
SelectFields_node1650488345488 = SelectFields.apply(
    frame=S3bucket_node1,
    paths=["col1", "col34", "col19"],
    transformation_ctx="SelectFields_node1650488345488",
)

# Script generated for node Select Fields
SelectFields_node1650489141747 = SelectFields.apply(
    frame=S3bucket_node1,
    paths=["col2", "col3", "col10", "col43", "col8"],
    transformation_ctx="SelectFields_node1650489141747",
)

# Script generated for node Drop Fields
DropFields_node1650488327748 = DropFields.apply(
    frame=SelectFields_node1650488262021,
    paths=["col2", "col3"],
    transformation_ctx="DropFields_node1650488327748",
)

# Script generated for node Drop Fields
DropFields_node1650489133218 = DropFields.apply(
    frame=SelectFields_node1650488345488,
    paths=["col3"],
    transformation_ctx="DropFields_node1650489133218",
)

# Script generated for node Drop Fields
DropFields_node1650646847636 = DropFields.apply(
    frame=SelectFields_node1650489141747,
    paths=["col1", "col4"],
    transformation_ctx="DropFields_node1650646847636",
)

# Script generated for node Amazon S3
AmazonS3_node1650489239075 = glueContext.getSink(
    path="s3://ta-s3-1/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1650489239075",
)
AmazonS3_node1650489239075.setCatalogInfo(
    catalogDatabase="tadata", catalogTableName="quality_measures.csv"
)
AmazonS3_node1650489239075.setFormat("csv")
AmazonS3_node1650489239075.writeFrame(DropFields_node1650488327748)
# Script generated for node Amazon S3
AmazonS3_node1650489266546 = glueContext.getSink(
    path="s3://ta-s3-1/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1650489266546",
)
AmazonS3_node1650489266546.setCatalogInfo(
    catalogDatabase="tadata", catalogTableName="bean_metadata.csv"
)
AmazonS3_node1650489266546.setFormat("csv")
AmazonS3_node1650489266546.writeFrame(DropFields_node1650489133218)
# Script generated for node Amazon S3
AmazonS3_node1650646870096 = glueContext.getSink(
    path="s3://ta-s3-1/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1650646870096",
)
AmazonS3_node1650646870096.setCatalogInfo(
    catalogDatabase="tadata", catalogTableName="farm_metadata.csv"
)
AmazonS3_node1650646870096.setFormat("csv")
AmazonS3_node1650646870096.writeFrame(DropFields_node1650646847636)
job.commit()
