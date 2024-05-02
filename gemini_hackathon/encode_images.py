import base64
import requests

def encode_gif(gif_image_path):
    with open(gif_image_path, "rb") as f:
        gif_bytes = f.read()
    thinking_gif_base64 = base64.b64encode(gif_bytes).decode()
    return thinking_gif_base64

def encode_image_url(image_url_path):
    response = requests.get(image_url_path)
    image_bytes = response.content
    image_base64 = base64.b64encode(image_bytes).decode()
    return image_base64