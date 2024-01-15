# Import necessary libraries
import requests
from twilio.rest import Client

# OpenWeatherMap API configuration
API_KEY = "ENTER YOUR API KEY"
OWN_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"

# Twilio API configuration
ACCOUNT_SID = 'TWILIO ACCOUNT SID' 
AUTH_TOKEN = 'TWILIO TOKEN'
TWILIO_NUMBER = "YOUR TWILIO NUMBER"
RECEIVER_NUMBER = "YOUR GSM NUMBER"
LATITUDE = "YOUR LATITUDE"  # Must be a float
LONGITUDE = "YOUR LONGITUDE"  # Must be a float

# Parameters for the OpenWeatherMap API request
parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
    "cnt": 4,
}

# Make the request to OpenWeatherMap API
response = requests.get(OWN_ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()

# Check if it will rain in the next 4 hours
will_rain = False
for hour_data in data["list"]:
    condition = int(hour_data["weather"][0]["id"])
    if condition < 700:
        will_rain = True

# If rain is expected, send a Twilio SMS alert
if will_rain:
    # Initialize Twilio client
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    # Send weather alert message
    message = client.messages.create(
        from_=TWILIO_NUMBER,
        body="It's going to rain today. Remember to bring an umbrella.",
        to=RECEIVER_NUMBER
    )

# Print the status of the Twilio message (optional)
print(message.status)
