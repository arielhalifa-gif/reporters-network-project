import os
import uuid
from fastapi import FastAPI
from app.config import IMAGES_PATH, RAW_TOPIC
from app.metadata import extract_metadata
from app.ocr import extract_text
from app.kafka_producer import publish
from app.mongo_client import send_binary

app = FastAPI()

@app.post("/ingest")
def ingest_images():
    for filename in os.listdir(IMAGES_PATH):

        image_path = os.path.join(IMAGES_PATH, filename)

        image_id = str(uuid.uuid4())

        metadata = extract_metadata(image_path)
        raw_text = extract_text(image_path)

        # send binary to Mongo Loader
        send_binary(image_path)

        # publish RAW event
        event = {
            "image_id": image_id,
            "raw_text": raw_text,
            "metadata": metadata
        }

        publish(RAW_TOPIC, event)

    return {"status": "done"}