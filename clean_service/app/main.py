import logging
from app.kafka_consumer import consume
from app.kafka_producer import publish
from app.cleaner import clean_text
from app.config import CLEAN_TOPIC

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run():

    logger.info("Clean Service started...")

    for event in consume():

        image_id = event["image_id"]
        raw_text = event["raw_text"]

        cleaned = clean_text(raw_text)

        new_event = {
            "image_id": image_id,
            "clean_text": cleaned
        }

        publish(CLEAN_TOPIC, new_event)

        logger.info(f"Processed image_id={image_id}")


if __name__ == "__main__":
    run()