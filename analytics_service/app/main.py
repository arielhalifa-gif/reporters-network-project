import logging
from app.kafka_consumer import consume
from app.kafka_producer import publish
from app.analytics import compute_metrics
from app.config import ANALYTICS_TOPIC

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run():

    logger.info("Analytics Service started...")

    for event in consume():

        image_id = event["image_id"]
        clean_text = event["clean_text"]

        metrics = compute_metrics(clean_text)

        analytics_event = {
            "image_id": image_id,
            **metrics
        }

        publish(ANALYTICS_TOPIC, analytics_event)

        logger.info(f"Analytics calculated for image_id={image_id}")


if __name__ == "__main__":
    run()