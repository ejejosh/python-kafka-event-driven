import json,logging
from kafka import KafkaProducer, KafkaConsumer

logging.basicConfig(level=logging.INFO)

ORDER_KAFKA_TOPIC = "order-details"
ORDER_PROCESSED_KAFKA_TOPIC = "order-processed"
BOOTSTRAP_SERVER = 'kafka-local.orders-microservice.svc.cluster.local:9092'

# Cosnsumer
consumer = KafkaConsumer(
    ORDER_KAFKA_TOPIC,
    bootstrap_servers = BOOTSTRAP_SERVER
)
# Producer
producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVER)


if __name__ == '__main__':
    logging.info("Started processing transaction...")
    while True:
        for message in consumer:
            consumed_message = json.loads(message.value.decode("utf-8"))

            username = consumed_message["username"]
            qty = consumed_message["quantity"]
            price = consumed_message["price"]
            total_cost = round(float(qty * price), 2)

            data = {
                "username": username,
                "order_id": consumed_message["order_id"],
                "email": consumed_message["email"],
                "total_cost": total_cost
            }
            logging.info(f"Transanction completed successfully...{data}")
            # Send message to process order topic
            producer.send(ORDER_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))
