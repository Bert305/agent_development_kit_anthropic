import datetime # Python library for the date and time
from zoneinfo import ZoneInfo # Python library for time zones
from google.adk.agents import Agent # Python library for Google Cloud AI Agent to activate (need a Google Cloud API key)
import requests # Python library for making HTTP requests witch will return a 200 status in the terminal if successful


# This Python function defines an agent that can answer questions about the time and weather in any US city.
def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified US city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    try:
        # Open-Meteo geocoding - is the process of converting place names or postal codes into geographical coordinates (latitude and longitude)
        
        
        # The Python get_weather function uses Open-Meteo geocoding API call to get lat/lon for the city
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&country=US&count=1"
        geo_resp = requests.get(geo_url, timeout=5)
        geo_resp.raise_for_status()
        geo_data = geo_resp.json()
        if not geo_data.get("results"):
            return {
                "status": "error",
                "error_message": f"Could not find location for '{city}'.",
            }
        lat = geo_data["results"][0]["latitude"]
        lon = geo_data["results"][0]["longitude"]
        resolved_city = geo_data["results"][0]["name"]

        # Get current weather data from Open-Meteo geocoding API
        weather_url = (
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
            "&current_weather=true&temperature_unit=fahrenheit"
        )
        # send a request to get current weather data
        weather_resp = requests.get(weather_url, timeout=5)
        weather_resp.raise_for_status()
        weather_data = weather_resp.json()
        current = weather_data.get("current_weather")
        if not current:
            return {
                "status": "error",
                "error_message": f"Weather information for '{city}' is not available.",
            }
        # Extract temperature and weather code using the formula to Convert Temperature
        temp_f = current["temperature"]
        temp_c = round((temp_f - 32) * 5 / 9, 1)
        weather_code = current.get("weathercode", "")
        # Simple mapping for weather code (for demo)
        weather_desc = "Clear" if weather_code == 0 else "Cloudy or Precipitation"
        # return success report
        return {
            "status": "success",
            "report": (
                f"The weather in {resolved_city} is {weather_desc} with a temperature of "
                f"{temp_c}°C ({temp_f}°F)."
            ),
        }
    # handle exceptions
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Failed to retrieve weather for '{city}': {e}",
        }

# The Python get current time function uses Open-Meteo geocoding api to get the current time of the city
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified US city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """
    try:
        # Use Open-Meteo geocoding API call to get lat/lon and timezone for the city
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&country=US&count=1"
        geo_resp = requests.get(geo_url, timeout=5)
        geo_resp.raise_for_status()
        geo_data = geo_resp.json()
        if not geo_data.get("results"):
            return {
                "status": "error",
                "error_message": f"Could not find location for '{city}'.",
            }
        # Extract Timezone & City
        tz_identifier = geo_data["results"][0]["timezone"]
        resolved_city = geo_data["results"][0]["name"]
        # Get the current time in the specified timezone
        tz = ZoneInfo(tz_identifier)
        now = datetime.datetime.now(tz)
        report = (
            f'The current time in {resolved_city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
        )
        return {"status": "success", "report": report} # success response
    
    # Error Handling
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Failed to retrieve time for '{city}': {e}",
        }

# Define the agent with the tools for weather and time retrieval
root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about the time and weather in any US city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in any US city."
    ),
    tools=[get_weather, get_current_time],
)


