from PIL import Image
import requests
from io import BytesIO


def display_img(image_url):
    #dispalying the preview image to make sure we're actually getting them
    responce = requests.get(image_url)
    img = Image.open(BytesIO(responce.content))
    img.show()


