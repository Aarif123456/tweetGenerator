# read files to create target list 
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, TimestampType, DecimalType, StringType, DoubleType
from pprint import pprint
from warnings import warn
from os import path


# read data from csv file
def readTweetData(file_path: str, spark: SparkSession, schema: StructType):
    return spark.read.option("multiLine", True) \
        .option("header", True) \
        .option("escape", "\"") \
        .schema(schema) \
        .csv(path=file_path, inferSchema=(schema == None), enforceSchema=(schema != None), header=True)


def writeListToFile(file_path: str, names: list, debug=False):
    if debug:
        pprint(names)
    with open(file_path, "w") as myfile:
        myfile.write("username\n")
        for name in names:
            myfile.write(name + "\n")


def readTargetList(spark: SparkSession, file_path='Output/targetList.txt'):
    df = spark.read.csv(path=file_path, \
                        inferSchema=True, \
                        header=True)
    return [i.username for i in df.select('username').collect()]


def extractTarget(spark: SparkSession, \
                  file_paths: list, \
                  schemas: list, \
                  debug=False,
                  output_file="Output/targetList.txt") -> list:
    if len(file_paths) != len(schemas):
        raise Exception("ERROR: file_paths and schema must be the same length")
    names_set = set()
    for i in range(len(file_paths)):
        if not path.exists(file_paths[i]):
            warn("Please download csv files from https://www.kaggle.com/manchunhui/us-election-2020-tweets")
            return readTargetList(spark)
        df = readTweetData(file_paths[i], spark, schemas[i])
        names = set([i.user_screen_name for i in df.select('user_screen_name').distinct().collect()])
        names_set = names_set.union(names)
    names_list = list(names_set)
    writeListToFile(output_file, names_list, debug)
    return names_list

# df[['tweet_id','tweet']].show(10)
# df=df.drop(*drop_cols)
# df.show(10)


# df.printSchema()
# print(df.dtypes)
