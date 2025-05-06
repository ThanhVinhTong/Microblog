import logging, os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_babel import Babel

from config import Config

from logging.handlers import SMTPHandler, RotatingFileHandler

def get_locale():
    # Try to get locale from cookie first
    locale = request.cookies.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    # Fall back to best match from accept-languages header
    return request.accept_languages.best_match(app.config['LANGUAGES'])

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

moment = Moment(app)
babel = Babel(app, locale_selector=get_locale)

login = LoginManager(app)
login.init_app(app)
login.login_message = 'Please log in to access this page.'
login.login_view = 'login'

mail = Mail(app)

# Log errors by email
if not app.debug:
    if app.config['MAIL_SERVER']:
        auth, secure = None, None

        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])

        if app.config['MAIL_USE_TLS']:
            secure = ()

        mail_handler = SMTPHandler (
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure
        )

        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    # Logging to a file
    if not os.path.exists('logs'):
        os.mkdir('logs')

    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

from app import routes, models, errors