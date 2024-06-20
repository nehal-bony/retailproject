from pyspark.sql import SparkSession

if __name__ == '__main__':

    print('Creating spark session')

    spark = SparkSession.builder \
    .appName ("Streaming application") \
    .master("local[2]") \
    .getOrCreate()

