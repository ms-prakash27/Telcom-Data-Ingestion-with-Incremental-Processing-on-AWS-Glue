import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

subsDf = glueContext.create_dynamic_frame.from_catalog(
    database="telcom_catalog",
    table_name="customer_subscription_2023_08_21_csv"
    )

subsDf.printSchema()
sparkSubsDf = subsDf.toDF()
sparkSubsDf.show()
print(sparkSubsDf.count())