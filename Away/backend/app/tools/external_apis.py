from typing import Any, Dict
import requests

def get_google_places_data(api_key: str, location: str, radius: int, type: str) -> Dict[str, Any]:
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={type}&key={api_key}"
    response = requests.get(url)
    return response.json()

def get_weather_data(api_key: str, location: str) -> Dict[str, Any]:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    return response.json()