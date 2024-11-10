from kafka import KafkaConsumer, TopicPartition

consumer = KafkaConsumer('simple', bootstrap_servers=['localhost:9092'])

for msg in consumer:
    print (msg)
