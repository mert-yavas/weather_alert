# Weather Alert Program
## Overview
Hello! I'm Mert, and today is Day 35 of my "100 Days of Python" challenge.  I'm sharing a Weather Alert Program developed on my journey through the This Python script provides weather alerts via Twilio SMS when rain is expected in the next 12 hours.

## Program Description
The Weather Alert Program checks OpenWeatherMap API for upcoming weather conditions and sends an SMS alert if rain is forecasted. It utilizes the Twilio API for sending messages and requires user configuration for API keys, phone numbers, and location coordinates.

## How to Run
To use the Weather Alert Program, follow these steps:

* Open the Python script: `main.py`
   ```bash
   python main.py
   ```

* Fill in your OpenWeatherMap API key, Twilio API credentials, and location coordinates.
* Run the script to check for weather conditions and receive SMS alerts.
* Make sure you have Python installed on your system.

## Configuration
Update the following variables in the script with your information:

* API_KEY: Your OpenWeatherMap API key.
* ACCOUNT_SID: Your Twilio account SID.
* AUTH_TOKEN: Your Twilio authentication token.
* TWILIO_NUMBER: Your Twilio phone number.
* RECEIVER_NUMBER: Your GSM number for receiving alerts.
* LATITUDE: Your location's latitude (must be a float).
* LONGITUDE: Your location's longitude (must be a float).
## Project Files
* main.py: The main Python script for the Weather Alert Program.
## Getting Started
* Fill in your API keys, Twilio credentials, and location coordinates.
* Run the script to check for upcoming weather conditions and receive SMS alerts.
* Alternatively, you can set daily tasks and make them automatic by installing this programme at https://www.pythonanywhere.com/.
## Used Libraries
The Weather Alert Program uses the following Python libraries:

* requests: For making API requests to OpenWeatherMap.
* twilio: For sending SMS alerts.
## Educational Insights
This project offers practical experience with the following Python concepts:

* API Integration: Interacting with OpenWeatherMap and Twilio APIs.
* Data Parsing: Extracting relevant information from API responses.
* Conditional Statements: Implementing checks for weather conditions.
* External Libraries: Utilizing requests and twilio libraries for functionality.
## Conclusion
I hope you find the Weather Alert Program useful for staying informed about upcoming rain. It's been an exciting journey, and I look forward to sharing more projects. Happy coding!
