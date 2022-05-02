from decouple import config
from dotenv import load_dotenv

load_dotenv()

# Discord
bot_token: str = config("bot_token")
bot_prefix = "/cmd "

# Redis
redis_user = config("redis_user")
redis_pass = config("redis_pass")
redis_port = config("redis_port")
redis_host = config("redis_host")