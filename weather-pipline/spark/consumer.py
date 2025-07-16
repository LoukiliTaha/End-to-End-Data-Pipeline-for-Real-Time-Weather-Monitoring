from pyspark.sql import  SparkSession
from pyspark.sql.functions import from_json , col
from pyspark.sql.types import *


schema = StructType([
    StructField("name", StringType(), True),  # City name

    StructField("main", StructType([
        StructField("temp", DoubleType(), True),
        StructField("humidity", IntegerType(), True)
    ]), True),

    StructField("weather", ArrayType(StructType([
        StructField("main", StringType(), True),
        StructField("description", StringType(), True)
    ])), True),

    StructField("dt", LongType(), True)  # Unix timestamp
])

spark = SparkSession.builder.appName("WeatherStream").getOrCreate()

df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "kafka:9092") \
  .option("subscribe", "weather_data") \
  .load()

weather_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")


# Store to PostgreSQL
weather_df.writeStream \
    .foreachBatch(lambda batch_df, _: batch_df.write
        .format("jdbc")
        .option("url", "jdbc:postgresql://postgres:5432/weather")
        .option("dbtable", "weather_data")
        .option("user", "postgres")
        .option("password", "postgres")
        .mode("append")
        .save()) \
    .start() \
    .awaitTermination()