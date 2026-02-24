import json
from confluent_kafka import Consumer
from app.config import KAFKA_BOOTSTRAP, CLEAN_TOPIC, GROUP_ID

consumer = Consumer({
    "bootstrap.servers": KAFKA_BOOTSTRAP,
    "group.id": GROUP_ID,
    "auto.offset.reset": "earliest"
})

consumer.subscribe([CLEAN_TOPIC])

def consume():
    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            continue

        yield json.loads(msg.value().decode("utf-8"))