import requests
import json

API_URL = "https://68170b1326a599ae7c392e16.mockapi.io/api/v1/pipelines/users"

def fetch_metrics():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"🚨 API Error: {e}")
        return []

if __name__ == "__main__" :
    pipelines = fetch_metrics()
    print(json.dumps(pipelines, indent=2))