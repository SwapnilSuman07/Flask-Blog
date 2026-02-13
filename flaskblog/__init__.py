import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

'''
app.config['SECRET_KEY'] = 'c9668c9a2b184599dc04d03bf488b98b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Mail config (Gmail)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
#app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
#app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

app.config['MAIL_USERNAME'] = 'swapnilsuman06@gmail.com'
app.config['MAIL_PASSWORD'] = 'ccvtbazdiksdhlux'
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

#print("MAIL_USERNAME =", app.config['MAIL_USERNAME'])
#print("MAIL_DEFAULT_SENDER =", app.config['MAIL_DEFAULT_SENDER'])
'''

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app