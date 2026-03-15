from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RetailStreaming").getOrCreate()

df = spark.readStream \
    .format("json") \
    .load("s3://retail-data-lake/raw/")

df.writeStream \
    .format("delta") \
    .option("checkpointLocation", "/checkpoints/bronze") \
    .start("s3://retail-data-lake/bronze/")
