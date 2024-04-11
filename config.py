from os import getenv

from dotenv import load_dotenv

load_dotenv()

DEBUG = False
BOT_TOKEN = getenv('BOT_TOKEN')
SQLALCHEMY_DATABASE_URL = getenv('SQLALCHEMY_DATABASE_URL')