import requests
import json
from pathlib import Path

API_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

def fetch_earthquake_data():
    response = requests.get(API_URL)
    response.raise_for_status()

    data = response.json()

    output_dir = Path("sample_data")
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "earthquake_raw_data.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
        print(f"Data saved successfully to {output_file}")

if __name__ == "__main__":
    fetch_earthquake_data()