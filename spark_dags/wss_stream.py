from pyspark.sql import SparkSession
import os
from pyspark.sql.functions import *

spark = SparkSession \
    .builder \
    .appName("StructuredNetworkWordCount") \
    .getOrCreate()

df = spark.readStream \
      .format("socket") \
      .option("host","test-ws.skns.dev/raw-messages") \
      .option("port","80") \
      .load()

result = df.writeStream \
  .format("console") \
  .start()

result.awaitTermination()
