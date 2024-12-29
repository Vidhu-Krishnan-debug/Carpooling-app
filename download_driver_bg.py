import os
import requests
from PIL import Image
from io import BytesIO

def download_and_save_image(url, save_path, size=None):
    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        
        if size:
            image = image.resize(size, Image.Resampling.LANCZOS)
        
        image.save(save_path, quality=85, optimize=True)
        print(f"Downloaded and saved: {save_path}")
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")

def download_driver_bg():
    base_path = os.path.join(os.path.dirname(__file__), 'static', 'images')
    url = 'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d'
    save_path = os.path.join(base_path, 'driver-bg.jpg')
    download_and_save_image(url, save_path, (1920, 1080))

if __name__ == "__main__":
    download_driver_bg()
