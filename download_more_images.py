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

def download_more_images():
    base_path = os.path.join(os.path.dirname(__file__), 'static', 'images')
    
    # Additional luxury cars
    cars = [
        ('https://images.unsplash.com/photo-1503376780353-7e6692767b70', 'luxury-car-5.jpg'),  # Porsche
        ('https://images.unsplash.com/photo-1580273916550-e323be2ae537', 'luxury-car-6.jpg'),  # Tesla
        ('https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8', 'luxury-car-7.jpg'),  # Range Rover
        ('https://images.unsplash.com/photo-1494976388531-d1058494cdd8', 'luxury-car-8.jpg'),  # Ferrari
    ]
    
    # Additional driver avatars
    avatars = [
        ('https://images.unsplash.com/photo-1560250097-0b93528c311a', 'driver-5.jpg'),
        ('https://images.unsplash.com/photo-1573496359142-b8d87734a5a2', 'driver-6.jpg'),
        ('https://images.unsplash.com/photo-1544005313-94ddf0286df2', 'driver-7.jpg'),
        ('https://images.unsplash.com/photo-1519085360753-af0119f7cbe7', 'driver-8.jpg'),
    ]
    
    # Download car images
    for url, filename in cars:
        save_path = os.path.join(base_path, 'cars', filename)
        download_and_save_image(url, save_path, (800, 600))
    
    # Download avatar images
    for url, filename in avatars:
        save_path = os.path.join(base_path, 'avatars', filename)
        download_and_save_image(url, save_path, (200, 200))

if __name__ == "__main__":
    download_more_images()
