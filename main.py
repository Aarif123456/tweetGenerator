from pyspark.sql.types import StructType, StructField, TimestampType, DecimalType, StringType, DoubleType
from pySparkManager import createSpark
from createTargetList import extractTarget
from createCorpus import createCorpusForUser
from generateResponse import generateTweet

# structure from tweet 
dtypes = StructType([StructField("created_at", TimestampType(), True), \
         StructField("tweet_id", StringType(), False), \
         StructField("tweet", StringType(), False), \
         StructField("likes", DecimalType(38, 0), False), \
         StructField("retweet_count", DecimalType(38, 0), False), \
         StructField("source", StringType(), True), \
         StructField("user_id", DecimalType(38, 0), False), \
         StructField("user_name", StringType(), True), \
         StructField("user_screen_name", StringType(), False), \
         StructField("user_description", StringType(), True), \
         StructField("user_join_date", TimestampType(), True), \
         StructField("user_followers_count", DecimalType(38, 0), False), \
         StructField("user_location", StringType(), True), \
         StructField("lat", DoubleType(), True), \
         StructField("long", DoubleType(), True), \
         StructField("city", StringType(), True), \
         StructField("country", StringType(), True), \
         StructField("continent", StringType(), True), \
         StructField("state", StringType(), True), \
         StructField("state_code", StringType(), True), \
         StructField("collected_at", TimestampType(), False) \
        ])
'''
If you want to just run the program on a specific individual 
uncomment the lines below
if you want you can change the url to something you want
'''
#name = "the_twitter_username"
#url = "https://t.co/bqa5pIAOnk"
# createCorpusForUser(name)
# generateTweet(name, url)

if __name__ == "__main__":
    file_paths = ["Resources/hashtag_donaldtrump.csv", "Resources/hashtag_joebiden.csv"]
    schemes = [dtypes, dtypes]
    spark = createSpark("tweet creator")
    names = extractTarget(spark, file_paths, schemes)
    # link to some random article
    url = "https://t.co/bqa5pIAOnk" 
    for name in names:
        createCorpusForUser(name)
        generateTweet(name, url)
    spark.stop()
