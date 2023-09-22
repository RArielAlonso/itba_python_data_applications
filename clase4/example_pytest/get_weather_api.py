import requests
def get_weather(lat, long):
    """
    Fetch and return the relative location's properties for the specified
    coordinates.
    Example: https://api.weather.gov/points/38.8894,-77.0352
    Args:
    lat: Latitude coordinate
    long: Longitude coordinate
    Returns:
    dict: The properties of the relative location.
    """
    base_url = "https://api.weather.gov/points/"
    response = requests.get(f"{base_url}{lat},{long}")
    data = response.json()
    if 'properties' not in data.keys():
        raise Exception("Value of coordinates are not correct, retry")
    else:
        return data['properties']['forecastHourly']