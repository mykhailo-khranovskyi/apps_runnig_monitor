import subprocess
from datetime import datetime

# Paths to your bot scripts
BOT_SCRIPTS = [
    'telegram_bot.py',
    'fair_share_bot.py',
    '/root/promise_roulette/myenv/bin/python3 promise_roulette_app.py',
    'baby_menu_bot.py',
    'imperia_game_bot.py',
    'nintendo_prices_bot.py'
]

def check_bots():
    running_bots = []
    for bot_script in BOT_SCRIPTS:
        result = subprocess.run(['ps', '-ef'], capture_output=True, text=True)
        if bot_script in result.stdout:
            running_bots.append(bot_script)
        else:
            print(f"Bot {bot_script} is down!")
    if running_bots:
        print("All bots are up and running!")

def main():
    # Start checking the bots
    check_bots()

if __name__ == "__main__":
    main()
