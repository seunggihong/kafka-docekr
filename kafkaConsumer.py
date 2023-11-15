from kafka import KafkaConsumer
import time

topic_name = 'topic_test'
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=['localhost:9092'],
    group_id='my-group'
)

start = time.time()
print('[begin] Topic: recive message from %s' % (topic_name))
for message in consumer:
    print("Partition : %d, Offset : %d, Value: %s" %
          (message.partition, message.offset, message.value))
print("[end] time taken : ", time.time() - start)
