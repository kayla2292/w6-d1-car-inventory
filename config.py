import os

basedir = os.path.abspath(os.path.dirname(__file__))
#give access to project in ANY operating system we find ourselves in
# allows outside files/folders to be added to project
#from base directory

class Config():
    """
    Set Config variables for the flask app.
    Using Environment Variables where available otherwise
    create the config variable if not done already
    """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'whats up'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turn off update messages ffrom sqlalchemy