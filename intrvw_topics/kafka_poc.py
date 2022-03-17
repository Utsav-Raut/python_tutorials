import json
from pyspark.sql import functions as F
import pyspark.sql.functions as func
brokers, topic = "PLAINTEXT://:9093,PLAINTEXT://:9094,PLAINTEXT://:9095" , 'my-kafka-topic'
startingOffsets = {topic:{"0":-2}}
startingOffsets[topic]["0"] = 0
endingOffsets = {topic:{"0":-1}}

df = (spark 
    .read
    .format("kafka") 
    .option("kafka.bootstrap.servers", brokers) 
    .option("subscribe", topic) 
    .option("startingOffsets", json.dumps(startingOffsets))
    .option("endingOffsets", json.dumps(endingOffsets))
    .option("failOnDataLoss",False)
    .load())

print(df)