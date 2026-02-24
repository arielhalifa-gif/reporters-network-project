import os
from dotenv import load_dotenv

load_dotenv()

KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP")
CLEAN_TOPIC = os.getenv("CLEAN_TOPIC")
ANALYTICS_TOPIC = os.getenv("ANALYTICS_TOPIC")
GROUP_ID = os.getenv("ANALYTICS_GROUP_ID")