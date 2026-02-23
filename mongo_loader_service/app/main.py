from fastapi import FastAPI, UploadFile, File
from pymongo import MongoClient
import gridfs
from app.config import MONGO_URI

app = FastAPI()

client = MongoClient(MONGO_URI)
db = client["images_db"]
fs = gridfs.GridFS(db)

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    content = await file.read()
    fs.put(content, filename=file.filename)
    return {"status": "saved"}