from kafka import KafkaProducer
import time
from dotenv import load_dotenv
import os

load_dotenv()

TOPIC_NAME = os.getenv("TOPIC_NAME")
PORT = os.getenv("PORT")

topic_name = TOPIC_NAME
producer = KafkaProducer(bootstrap_servers=[PORT])

start = time.time()
print('[begin] start sending message from producer')

for i in range(10000):
    data = {'str': 'result' + str(i)}
    print('sending message...'+data['str'])
    producer.send(topic_name, value=data)
    producer.flush()

print('[end] time taken', time.time() - start)
