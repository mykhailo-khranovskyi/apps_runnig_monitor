# apps_runnig_monitor - Monitor running apps and send notifications to Telegram
# create a config.py file with the following content:
    TOKEN = 'token' # Telegram bot token
    YOUR_CHAT_ID = 'id' # Your chat id
# python3 -m venv venv
# source venv/bin/activate
# pip3 install pyTelegramBotAPI, schedule
# nohup python3 apps_running_monitor.py & # Run in background