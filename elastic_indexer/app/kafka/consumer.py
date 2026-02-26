from confluent_kafka import Consumer
from app.config import KAFKA_BOOTSTRAP

def create_consumer(group_id: str):
    conf = {
        "bootstrap.servers": KAFKA_BOOTSTRAP,
        "group.id": group_id,
        "auto.offset.reset": "earliest"
    }
    return Consumer(conf)