from kafka import KafkaConsumer
import time
from dotenv import load_dotenv
import os

load_dotenv()

TOPIC_NAME = os.getenv("TOPIC_NAME")
GROUP_ID = os.getenv("GROUP_ID")
PORT = os.getenv("PORT")

topic_name = TOPIC_NAME
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=[PORT],
    group_id=GROUP_ID
)

start = time.time()
print('[begin] Topic: recive message from %s' % (topic_name))
for message in consumer:
    print("Partition : %d, Offset : %d, Value: %s" %
          (message.partition, message.offset, message.value))
print("[end] time taken : ", time.time() - start)
