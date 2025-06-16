# Wayside 🌊

A simple Waybar configuration for Sway with Google Calendar integration. ✨

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/koyuawsmbrtn/wayside
```

2. Install Python dependencies: 🐍
```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib --user --break-system-packages
```

3. Get Google Calendar credentials: 📅
   - Go to [Google Cloud Console](https://console.cloud.google.com)
   - Create a new project or select an existing one
   - Enable the Google Calendar API
   - Create OAuth 2.0 credentials
   - Download the credentials and save as `credentials.json` in the wayside directory

4. Generate authentication token: 🔑
```bash
python gcal_fetch.py
```

5. Copy the configuration files to your config directory: 📁
```bash
cp -r wayside ~/.config/
```

6. Add the following line to your Sway config file (`~/.config/sway/config`): ⚙️
```bash
exec waybar -c ~/.config/wayside/waybar_config.json
```

7. Create a todo.txt file in your home directory: 📝
```bash
touch ~/todo.txt
```

8. Restart Sway or launch Waybar manually 🔄

## 🧩 Components

- `gcal_fetch.py` - Fetches upcoming events from Google Calendar 📅
- `convert_text.py` - Utility script for converting newlines to carriage returns ↩️
- `waybar_config.json` - Waybar configuration with calendar and todo widgets 🎯

The calendar widget updates every 5 minutes and the todo widget updates every 3 seconds. ⏱️

## 📋 Requirements

- Sway
- Waybar
- Python 3
- Google Calendar API credentials

## 📜 License

**MIT License**

Feel free to modify and use this configuration as you wish. Contributions are