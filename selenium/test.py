from internet_speed_twitter_bot import InternetSpeedTwitterBot
bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
print(f"Down: {bot.download_speed}; Up: {bot.upload_speed}")