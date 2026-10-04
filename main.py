import requests
import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_BOT_TOKEN=os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID=os.environ.get("TELEGRAM_CHAT_ID")
WEATHER_API_KEY=os.environ.get("WEATHER_API_KEY")
parameters = {
    "lat":41.299496,
    "lon":69.240074,
    "appid":WEATHER_API_KEY,
    "cnt":8,
    "units":"metric",

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()


def build_weather_message(forecast):
    weather = forecast["weather"][0]
    condition_id = int(weather["id"])
    description = weather["description"].title()
    temp = forecast["main"]["temp"]

    if condition_id < 300:
        emoji, advice = "⚡", "Stay indoors"
    elif condition_id < 400:
        emoji, advice = "🌦", "Light drizzle, maybe an umbrella"
    elif condition_id < 600:
        emoji, advice = "☔", "Bring an umbrella"
    elif condition_id < 700:
        emoji, advice = "❄️", "Wear warm clothes"
    elif condition_id == 781:
        emoji, advice = "🌪", "SEEK SHELTER NOW"
    elif condition_id < 800:
        emoji, advice = "🌫", "Drive carefully"
    else:
        emoji, advice = "☀️", ""

    parts = [f"{emoji} {description}"]
    if advice:
        parts.append(advice)
    parts.append(f"🌡 {temp}°C")

    return "\n".join(parts)



def get_alert_level(forecast):
    """Return severity: higher = worse weather."""
    condition_id = int(forecast["weather"][0]["id"])

    if condition_id == 781:      # tornado
        return 5
    if condition_id < 300:       # thunderstorm
        return 4
    if condition_id < 600:       # rain, drizzle
        return 3
    if condition_id < 700:       # snow
        return 4
    if condition_id < 800:       # fog, mist
        return 2
    return 1                     # clear / cloudy


def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    response = requests.post(
        url,
        data={
            "chat_id":TELEGRAM_CHAT_ID,
            "text":text,
        },
        timeout=10,
    )
    response.raise_for_status()

worst_forecast = None
worst_level = 0

for forecast in weather_data["list"]:
    level = get_alert_level(forecast)
    if level > worst_level:
        worst_level = level
        worst_forecast = forecast

print(f"Worst weather level: {worst_level}")

if worst_level >= 3:
    message = build_weather_message(worst_forecast)
    send_to_telegram(f"⚠️ Weather Alert\n\n{message}")
    print("Alert sent to Telegram ✅")
else:
    print("Weather is fine. No alert sent.")