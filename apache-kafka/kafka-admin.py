from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id="my_admin_client")

new_topic = NewTopic(
    name="simple",
    num_partitions=1,
    replication_factor=1
)

admin_client.create_topics([new_topic])
