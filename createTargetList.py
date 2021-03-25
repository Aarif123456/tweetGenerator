# read files to create target list 
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, TimestampType, DecimalType, StringType, DoubleType
from pprint import pprint
from warnings import warn
from os import path


# read data from csv file
def readTweetData(filePath: str, spark: SparkSession, schema: StructType):
    return spark.read.option("multiLine", True) \
        .option("header", True) \
        .option("escape", "\"") \
        .schema(schema) \
        .csv(path=filePath, inferSchema=(schema == None), enforceSchema=(schema != None), header=True)


def writeListToFile(filePath: str, names: list, debug=False):
    if debug:
        pprint(names)
    with open(filePath, "w") as myfile:
        myfile.write("username\n")
        for name in names:
            myfile.write(name + "\n")


def readTargetList(spark: SparkSession, filePath='Output/targetList.txt'):
    df = spark.read.csv(path=filePath, \
                        inferSchema=True, \
                        header=True)
    return [i.username for i in df.select('username').collect()]


def extractTarget(spark: SparkSession, \
                  filePaths: list, \
                  schemas: list, \
                  debug=False,
                  outputFile="Output/targetList.txt") -> list:
    if len(filePaths) != len(schemas):
        raise Exception("ERROR: filePaths and schema must be the same length")
    namesSet = set()
    for i in range(len(filePaths)):
        if not path.exists(filePaths[i]):
            warn("Please download csv files from https://www.kaggle.com/manchunhui/us-election-2020-tweets")
            return readTargetList(spark)
        df = readTweetData(filePaths[i], spark, schemas[i])
        names = set([i.user_screen_name for i in df.select('user_screen_name').distinct().collect()])
        namesSet = namesSet.union(names)
    names_list = list(namesSet)
    writeListToFile(outputFile, names_list, debug)
    return names_list

# df[['tweet_id','tweet']].show(10)
# df=df.drop(*drop_cols)
# df.show(10)


# df.printSchema()
# print(df.dtypes)
