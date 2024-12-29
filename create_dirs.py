import os

def create_directories():
    base_path = os.path.join(os.path.dirname(__file__), 'static', 'images')
    directories = [
        base_path,
        os.path.join(base_path, 'cars'),
        os.path.join(base_path, 'avatars'),
        os.path.join(base_path, 'icons')
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")

if __name__ == "__main__":
    create_directories()
