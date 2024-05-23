import os
import PIL
from PIL import Image
import requests
import io
API_TOKEN="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"
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
def generate(user_input):
    def uniquify(path):
        filename, extension = os.path.splitext(path)
        counter = 1
        while os.path.exists(path):
            path = filename + " (" + str(counter) + ")" + extension
            counter += 1
        return path

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.content

    image_bytes = query({"inputs": user_input, })
    image = PIL.Image.open(io.BytesIO(image_bytes))
    image_path = uniquify(user_input+".png")
    image_path="image"+str(i)+".png"
    image.save(image_path)
    print(f"Image saved as {image_path}")
while True:
    prop = input("enter prompt: ")
    for i in range(1,9):
        generate(str(prop) + str(i))
