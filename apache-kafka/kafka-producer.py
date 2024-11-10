from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

for index in range(100):
    producer.send("simple", b"Message with index-{index} is sent")

producer.flush()
producer.close()
