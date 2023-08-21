from dotenv import load_dotenv, dotenv_values
import os

load_dotenv('.env')

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///users.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
	AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
	MY_NUMBER = os.environ.get('MY_NUMBER')
	TWILLIO_NUMBER = os.environ.get('TWILIO_NUMBER')
