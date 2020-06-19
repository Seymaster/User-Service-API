from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
import datetime

app = Flask(__name__, instance_relative_config=True)
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'myers12919@gmail.com',
    MAIL_PASSWORD = 'EVerything_123',
    MAIL_DEFAULT_SENDER = 'myers12919@gmail.com'
))

api = Api(app)
jwt = JWTManager(app)
mail = Mail(app)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# app.config['SQLACHEMY_DATABASE_URL']
# app.config['SQLACHEMY_TRACK_MODIFICATIONS']
# app.config['JWT_SECRET_KEY'] =  'secret'
# app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days = 1)
# app.config['JWT_TOKEN_LOCATION'] = "query_string"
# app.config['JWT_QUERY_STRING_NAME'] = "token"

db = SQLAlchemy(app)

from strapi.users.views import Usersapi,Confirmapi,Loginapi,Unconfirmapi,Resendapi
from strapi.service.views import Serviceapi,service_api
from strapi.contact.script import Contactapi,contact_api
service_api.add_resource(Serviceapi,'/services')
api.add_resource(Usersapi, '/signup')
api.add_resource(Loginapi, '/login')
api.add_resource(Confirmapi, '/confirm-email/<string:token>')
api.add_resource(Unconfirmapi, '/unconfirmed')
api.add_resource(Resendapi, '/resend-activation')
contact_api.add_resource(Contactapi, '/contact-us')
