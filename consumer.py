from kafka import KafkaConsumer
import json

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('json-topic',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest')

for message in consumer:
    print (message.value.decode('ascii'))


