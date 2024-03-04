import subprocess
import telebot
import schedule
import time
from config import TOKEN, YOUR_CHAT_ID

# Initialize the bot
bot = telebot.TeleBot(TOKEN)

# Paths to your bot scripts
BOT_SCRIPTS = [
    'telegram_bot.py',
    'fair_share_bot.py',
    '/root/promise_roulette/myenv/bin/python3 promise_roulette_app.py',
    'baby_menu_bot.py',
    'imperia_game_bot.py',
    'nintendo_prices_bot.py',
    'bot_analytics.py',
    'baby_menu_en.py',
]


def check_bots():
    running_bots = []
    for bot_script in BOT_SCRIPTS:
        result = subprocess.run(['ps', '-ef'], capture_output=True, text=True)
        if bot_script in result.stdout:
            running_bots.append(bot_script)
        else:
            bot.send_message(chat_id=YOUR_CHAT_ID, text=f"Bot {bot_script} is down!")
            print(f"Bot {bot_script} is down!")
    if not running_bots:
        bot.send_message(chat_id=YOUR_CHAT_ID, text="Not all bots are up and running!")
        print("Not all bots are up and running!")


def send_daily_status():
    check_bots()
    running_bots = "\n".join(BOT_SCRIPTS)
    status_message = f"Daily status check: Monitored bots/apps are:\n{running_bots}"
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
