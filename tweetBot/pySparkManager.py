# Use pySpark to handle large amount of data
import os
from pyspark.sql import SparkSession

# probably misconfiguration on my environment - but this forces PySpark to use Python 3
os.environ["PYSPARK_PYTHON"] = "/usr/bin/python3"


def createSpark(app_name: str):
    return SparkSession \
        .builder \
        .appName(app_name) \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
