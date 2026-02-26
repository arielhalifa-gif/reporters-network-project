from app.config import ELASTIC_INDEX

MAPPING = {
    "mappings": {
        "properties": {
            "file_name": {"type": "keyword"},
            "text_raw": {"type": "text"},
            "text_clean": {"type": "text"},
            "metadata": {"type": "object"},
            "top_10_words": {"type": "keyword"},
            "weapons_found": {"type": "keyword"},
            "sentiment.label": {"type": "keyword"},
            "sentiment.score": {"type": "float"}
        }
    }
}

def ensure_index(client):
    if not client.indices.exists(index=ELASTIC_INDEX):
        client.indices.create(index=ELASTIC_INDEX, body=MAPPING)