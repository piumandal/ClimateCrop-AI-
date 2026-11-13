
import requests

# Step 1: Get city coordinates
def get_city_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()

    data = response.json()

    if "results" not in data:
        return None

    return data["results"][0]


# Step 2: Get live weather
def get_live_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": [
            "temperature_2m",
            "relative_humidity_2m",
            "precipitation",
            "weather_code",
            "wind_speed_10m"
        ],
        "timezone": "auto"
    }

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()

    return response.json()


# Step 3: Ask city name
city = input("Enter your city name: ")

try:
    location = get_city_coordinates(city)

    if location is None:
        print("City not found. Please try another city.")
    else:
        latitude = location["latitude"]
        longitude = location["longitude"]

        print("\nCity:", location["name"])
        print("State:", location.get("admin1", "N/A"))
        print("Latitude:", latitude)
        print("Longitude:", longitude)

        weather = get_live_weather(latitude, longitude)
        current = weather["current"]

        print("\n----- LIVE WEATHER -----")
        print("Temperature:", current["temperature_2m"], "°C")
        print("Humidity:", current["relative_humidity_2m"], "%")
        print("Precipitation:", current["precipitation"], "mm")
        print("Weather Code:", current["weather_code"])
        print("Wind Speed:", current["wind_speed_10m"], "km/h")

except requests.RequestException as error:
    print("Weather API error:", error)
except (KeyError, IndexError) as error:
    print("Unexpected API response:", error)
