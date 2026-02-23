import os
from dotenv import load_dotenv

load_dotenv()

KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP")
RAW_TOPIC = os.getenv("RAW_TOPIC")

MONGO_LOADER_URL = os.getenv("MONGO_LOADER_URL")

IMAGES_PATH = os.getenv("IMAGES_PATH")