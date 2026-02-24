import os
from dotenv import load_dotenv

load_dotenv()

KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP")
RAW_TOPIC = os.getenv("RAW_TOPIC")
CLEAN_TOPIC = os.getenv("CLEAN_TOPIC")
GROUP_ID = os.getenv("CLEAN_GROUP_ID")