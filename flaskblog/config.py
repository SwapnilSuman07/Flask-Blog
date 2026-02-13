import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URL')

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    
class Config:
    SECRET_KEY = 'c9668c9a2b184599dc04d03bf488b98b'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    # Mail config (Gmail)
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'swapnilsuman06@gmail.com'
    MAIL_PASSWORD = 'ccvtbazdiksdhlux'
    #MAIL_DEFAULT_SENDER = 'MAIL_USERNAME'
    