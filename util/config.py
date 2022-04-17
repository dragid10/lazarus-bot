from dotenv import load_dotenv
from decouple import config

load_dotenv()

bot_token: str = config("bot_token")
bot_prefix = "/cmd "
