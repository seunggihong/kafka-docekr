from kafka import KafkaProducer
from json import dumps
import time

topic_name = 'topic_test'
producer = KafkaProducer(
    acks=0,
    compression_type='gzip',
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

start = time.time()
print('[begin] start sending message from producer')

for i in range(10000):
    data = {'str' : 'result' + str(i)}
    print('sending message...'+data['str'])
    producer.send(topic_name, value=data)
    producer.flush()
print('[end] time taken', time.time() - start)