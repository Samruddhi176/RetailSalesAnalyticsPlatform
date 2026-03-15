from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

spark = SparkSession.builder.appName("RetailStreaming").getOrCreate()

df = spark.read.format("delta").load("s3://retail-data-lake/silver/")

sales = df.groupBy("store_id") \
    .agg(sum("price").alias("total_sales"))

sales.write \
    .format("delta") \
    .mode("overwrite") \
    .save("s3://retail-data-lake/gold/sales_by_store")
