from dotenv import load_dotenv
import os

load_dotenv('.env')

DJANGO_KEY = os.environ.get('DJANGO_KEY')

print(DJANGO_KEY)
