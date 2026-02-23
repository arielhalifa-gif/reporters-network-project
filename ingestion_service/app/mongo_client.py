import requests
from app.config import MONGO_LOADER_URL

def send_binary(file_path: str):
    with open(file_path, "rb") as f:
        files = {"file": f}
        response = requests.post(MONGO_LOADER_URL, files=files)
    return response.status_code