from kafka import KafkaConsumer
from json import loads
import time

topic_name = 'topic_test'
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    consumer_timeout_ms = 1000
)

start = time.time()
print('[begin] Topic: recive message from %s'%(topic_name))
for message in consumer:
    print("Partition : %d, Offset : %d, Value: %s"%(message.partition, message.offset, message.value))
print("[end] time taken : ", time.time() - start )