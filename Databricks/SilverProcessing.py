from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RetailStreaming").getOrCreate()

df = spark.read.format("delta").load("s3://retail-data-lake/bronze/")

clean_df = df.dropDuplicates(["transaction_id"])

clean_df.write \
    .format("delta") \
    .mode("overwrite") \
    .save("s3://retail-data-lake/silver/")
