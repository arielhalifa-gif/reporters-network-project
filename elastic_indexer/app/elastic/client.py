from elasticsearch import Elasticsearch
from app.config import ELASTIC_HOST

def create_client():
    return Elasticsearch(ELASTIC_HOST)