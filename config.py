import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

class Config:
    API_TITLE = "RESTAURANT API"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    # SSL settings passed as 'connect_args'
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {
            'ssl': {
                'ca': os.path.join(os.getcwd(), 'app/certs/ca.pem')
            }
        }
    }