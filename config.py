import datetime
import os

DEBUG = True

# Globally database configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql://root@localhost/test1'
SQLACHEMY_TRACK_MODIFICATIONS = True

# JWT configuration
JWT_SECRET_KEY =  'secret'
JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days = 1)
JWT_TOKEN_LOCATION = "query_string"
JWT_QUERY_STRING_NAME = "token"

# Main Configuration
SECRET_KEY = "secret"
SECURITY_PASSWORD_SALT = "secret"

# Mail configurations
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = False
MAIL_USE_SSL = True 
MAIL_DEBUG = True
MAIL_DEFAULT_SENDER = "your@gmail.com"
MAIL_PASSWORD = "yourpassword"