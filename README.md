# Kafka Setting in Docker

## version

- docker : 24.0.6
- python3 : 3.6.9
- kafka : 3.6.0
- zookeeper: 3.4.6

  <a href = https://dlcdn.apache.org/kafka/3.6.0/kafka_2.13-3.6.0.tgz>Kafka download</a>

#

## Using

### Docker compose

- yml script 👉 <a href = https://github.com/seunggihong/kafka-docker/blob/main/docker-compose.yml >docker-compose.yml</a>

```
docker-compose -f docker-compose.yml up -d
```

### Container execute

```
docker exec -i -t {container-name} /bash
```

### Download kafka cdn

```
wget { kafka download link }
```

### Copy script

- Local terminal
- Python3 script 👉 <a href = https://github.com/seunggihong/kafka-docker/blob/main/kafkaProducer.py >kafkaProducer.py</a>, <a href = https://github.com/seunggihong/kafka-docker/blob/main/kafkaConsumer.py >kafkaConsumer.py</a>

```
docker cp kafkaProducer.py {container-name}:{path}
docker cp kafkaConsumer.py {container-name}:{path}
```

### Python3 install

```
apk --no-cache update
apk --no-cache add python3
```

### Starting script

```
python3 kafkaProducer.py
python3 kafkaConsumer.py
```

#

## 📌 Other

### Kafka Topic command

- create new topic

```
kafka-topic.sh --create --bootstrap-server localhost:{port} --topic {new-topic-name}
```

- topic check

```
kafka-topic.sh --list --zookeeper localhost
```

- topic delete

```
kafka-topic.sh --delete --zookeeper localhost --topic {topic-name}
```

#

## Reference

- https://kafka.apache.org/quickstart
