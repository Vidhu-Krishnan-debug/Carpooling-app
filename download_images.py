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

def download_sample_images():
    # Create directories if they don't exist
    base_path = os.path.join(os.path.dirname(__file__), 'static', 'images')
    
    # Sample image URLs (from Unsplash)
    images = {
        'cars': [
            ('https://images.unsplash.com/photo-1563720360172-67b8f3dce741', 'luxury-car-1.jpg'),  # Mercedes
            ('https://images.unsplash.com/photo-1556189250-72ba954cfc2b', 'luxury-car-2.jpg'),  # BMW
            ('https://images.unsplash.com/photo-1603584173870-7f23fdae1b7a', 'luxury-car-3.jpg'),  # Audi
            ('https://images.unsplash.com/photo-1617814076367-b759c7d7e738', 'luxury-car-4.jpg')   # Bentley
        ],
        'avatars': [
            ('https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d', 'driver-1.jpg'),
            ('https://images.unsplash.com/photo-1494790108377-be9c29b29330', 'driver-2.jpg'),
            ('https://images.unsplash.com/photo-1500648767791-00dcc994a43e', 'driver-3.jpg'),
            ('https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e', 'driver-4.jpg')
        ],
        'icons': [
            ('https://img.icons8.com/color/96/000000/money-bag.png', 'savings.png'),
            ('https://img.icons8.com/color/96/000000/groups.png', 'community.png'),
            ('https://img.icons8.com/color/96/000000/earth-planet.png', 'eco.png')
        ]
    }
    
    # Background images
    backgrounds = [
        ('https://images.unsplash.com/photo-1449965408869-eaa3f722e40d', 'hero-bg.jpg'),   # City road
        ('https://images.unsplash.com/photo-1532974297617-c0f05fe48bff', 'search-bg.jpg')  # Highway
    ]
    
    # Download car images
    for url, filename in images['cars']:
        save_path = os.path.join(base_path, 'cars', filename)
        download_and_save_image(url, save_path, (800, 600))
    
    # Download avatar images
    for url, filename in images['avatars']:
        save_path = os.path.join(base_path, 'avatars', filename)
        download_and_save_image(url, save_path, (200, 200))
    
    # Download icon images
    for url, filename in images['icons']:
        save_path = os.path.join(base_path, 'icons', filename)
        download_and_save_image(url, save_path)
    
    # Download background images
    for url, filename in backgrounds:
        save_path = os.path.join(base_path, filename)
        download_and_save_image(url, save_path, (1920, 1080))

if __name__ == "__main__":
    download_sample_images()
