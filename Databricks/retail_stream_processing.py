from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RetailStreaming").getOrCreate()

df = spark.readStream \
    .format("json") \
    .load("s3://retail-data-lake/raw/")

df.writeStream \
    .format("delta") \
    .option("checkpointLocation", "s3://retail-data-lake/checkpoints/") \
    .start("s3://retail-data-lake/bronze/")
