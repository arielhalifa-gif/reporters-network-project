from PIL import Image
import os

def extract_metadata(image_path: str) -> dict:
    with Image.open(image_path) as img:
        width, height = img.size
        format_file = img.format

    bytes_size_file = os.path.getsize(image_path)

    return {
        "bytes_size_file": bytes_size_file,
        "width": width,
        "height": height,
        "format_file": format_file
    }