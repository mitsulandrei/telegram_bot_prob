import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
WEATHER_TOKEN = str(os.getenv("WEATHER_TOKEN"))

admins_id = [
    5700591415
]