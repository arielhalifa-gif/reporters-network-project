from app.config import RAW_TOPIC, CLEAN_TOPIC, ANALYTICS_TOPIC

def extract_partial_document(topic: str, data: dict):
    """מחלץ partial document לפי סוג האירוע"""

    if topic == RAW_TOPIC:
        return {
            "file_name": data.get("file_name"),
            "metadata": data.get("metadata"),
            "text_raw": data.get("text_raw")
        }

    if topic == CLEAN_TOPIC:
        return {
            "text_clean": data.get("text_clean")
        }

    if topic == ANALYTICS_TOPIC:
        return {
            "top_10_words": data.get("top_10_words"),
            "weapons_found": data.get("weapons_found"),
            "sentiment": data.get("sentiment")
        }

    return {}