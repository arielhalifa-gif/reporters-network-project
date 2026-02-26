from app.config import ELASTIC_INDEX

class ElasticRepository:
    """ביצוע Upsert למסמך ב־Elasticsearch"""

    def __init__(self, client):
        self.client = client

    def upsert(self, id_image: str, document: dict):
        self.client.update(
            index=ELASTIC_INDEX,
            id=id_image,
            doc=document,
            doc_as_upsert=True
        )