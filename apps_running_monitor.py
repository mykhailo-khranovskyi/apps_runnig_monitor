import time
import telebot
import schedule
import subprocess
from config import TOKEN, YOUR_CHAT_ID

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

# Paths to your bot scripts, apps, etc.
BOT_SCRIPTS = [
    'getbikesbot.py',
    'fair_share_bot.py',
    'baby_menu_bot.py',
    'imperia_game_bot.py',
    'bot_analytics.py',
    'baby_menu_en.py',
    'mkhranovskyi:app',
    'baby_menu_lp:app',
    'cult_movies.py',
    'desktopgames_rent_bot.py' # https://t.me/desktopgames_rent_bot
]


# Function to check if the bots are running
def check_bots():
    running_bots = []
    for bot_script in BOT_SCRIPTS:
        result = subprocess.run(['ps', '-ef'], capture_output=True, text=True)
        if bot_script in result.stdout:
            running_bots.append(bot_script)
        else:
            bot.send_message(chat_id=YOUR_CHAT_ID, text=f"🍎Bot {bot_script} is down!")
            print(f"Bot {bot_script} is down!")
    if not running_bots:
        bot.send_message(chat_id=YOUR_CHAT_ID, text="🍎Not all bots are up and running!")
        print("Not all bots are up and running!")


# Function to send daily status
def send_daily_status():
    check_bots()
    running_bots = "\n 🙊".join(BOT_SCRIPTS)
    status_message = f"🍏Daily status check: Monitored bots/apps are:\n\n{running_bots}"
    bot.send_message(chat_id=YOUR_CHAT_ID, text=status_message)


def main():
    send_daily_status()
    # Schedule bot check every minute
    schedule.every().minute.do(check_bots)

    # Schedule status report every 5 minutes
    # schedule.every(3).minutes.do(send_daily_status)

    # Schedule bot check every hour
    # schedule.every().hour.do(check_bots)

    # Schedule daily status message
    schedule.every().day.at("07:00").do(send_daily_status)  # Adjust the time as needed
    schedule.every().day.at("17:00").do(send_daily_status)  # Adjust the time as needed

    # Infinite loop to keep the program running
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
