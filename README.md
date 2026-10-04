# 🌦 Weather Alert Bot

A Python bot that checks the weather forecast twice a day and sends you a
Telegram message **only when bad weather is coming** — rain, snow,
thunderstorm, or tornado.

Runs for free on GitHub Actions. No server, no cost.

---

## 🎯 What It Does

Twice a day (morning and evening), the bot:

1. Fetches the 24-hour weather forecast for Tashkent
2. Checks if any of the next 8 three-hour slots have bad weather
3. If yes → sends a Telegram alert with an emoji, description, and advice
4. If no → stays silent (no spam)

**Most days:** you get nothing.
**Bad weather days:** one clear, useful alert.

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| Telegram Alerts | Sends messages via your personal Telegram bot |
| Smart Severity | Ranks weather by severity (rain < snow < storm < tornado) |
| Context-Aware Emoji | ⚡ 🌦 ☔ ❄️ 🌪 🌫 ☀️ per condition |
| Human Advice | "Bring an umbrella", "Wear warm clothes", etc. |
| Runs Twice Daily | 8 AM and 6 PM Tashkent time |
| Silent When Safe | No spam on clear days |
| Free Forever | Powered by GitHub Actions |

---

## 📁 Project Structure
Weather-Alert/
├── .github/

│ └── workflows/

│ └── weather.yml # GitHub Actions schedule

├── main.py # Main script

├── requirements.txt # Dependencies

├── .gitignore # Ignored files

└── README.md # Documentation

---

## 🛠️ Technologies Used

- **Python 3.12**
- **OpenWeatherMap API** — weather forecast data
- **Telegram Bot API** — sending messages
- **GitHub Actions** — free scheduled runs
- **requests** — HTTP calls

---
## 🚀 Setup

### 1. Clone the repository

```bash
git clone git@github.com:your-username/weather-alert-bot.git
cd weather-alert-bot
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
# or: .venv\Scripts\activate     # Windows
pip install -r requirements.txt