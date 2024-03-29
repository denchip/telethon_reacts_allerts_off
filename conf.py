import os
import json
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_ID = os.getenv('TELEGRAM_API_ID')
TELEGRAM_API_HASH = os.getenv('TELEGRAM_API_HASH')
CHAT_IDS = json.loads(os.getenv('CHAT_IDS'))
