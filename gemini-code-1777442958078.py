import requests

def get_weather(city):
    # Using Open-Meteo (A free API that doesn't require an API Key for basic use)
    # First, we get coordinates for the city name
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"
    
    try:
        geo_res = requests.get(geo_url).json()
        if not geo_res.get("results"):
            return "City not found. Check your spelling!"

        location = geo_res["results"][0]
        lat, lon = location["latitude"], location["longitude"]

        # Now, fetch the actual weather using those coordinates
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_res = requests.get(weather_url).json()
        
        temp = weather_res["current_weather"]["temperature"]
        wind = weather_res["current_weather"]["windspeed"]

        return (f"--- Weather in {location['name']}, {location['country']} ---\n"
                f"Temperature: {temp}°C\n"
                f"Wind Speed: {wind} km/h")

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("Welcome to the Mini Weather App!")
    user_city = input("Enter a city name: ")
    print(get_weather(user_city))