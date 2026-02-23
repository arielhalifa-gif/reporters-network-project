import json
from confluent_kafka import Producer
from app.config import KAFKA_BOOTSTRAP

producer = Producer({
    "bootstrap.servers": KAFKA_BOOTSTRAP
})

def publish(topic: str, message: dict):
    producer.produce(
        topic,
        value=json.dumps(message).encode("utf-8")
    )
    producer.flush()