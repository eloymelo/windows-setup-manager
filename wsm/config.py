from pathlib import Path
import yaml

def get_packages():
    current_dir = Path(__file__).parent
    file_path = current_dir.parent / 'config' / 'packages.yaml'

    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)       
    return data

def save_packages(package_data):
    current_dir = Path(__file__).parent
    file_path = current_dir.parent / 'config' / 'packages.yaml'

    with open(file_path, 'w') as f:
        yaml.dump(package_data, f)