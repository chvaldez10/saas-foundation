import requests
from pathlib import Path

def download_to_local(url: str, output_path: Path, parent_mkdir: bool = True):

    if not isinstance(output_path, Path):
        raise ValueError("output_path must be a Path object")

    if parent_mkdir:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
    try:
        response = requests.get(url)
        response.raise_for_status()
        output_path.write_bytes(response.content)
        return True
    except requests.RequestException as e:
        print(f"Error downloading {url}: {e}")
        return False
