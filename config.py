import os
basedir = os.path.abspath(os.path.dirname(__file__))
class config(object):
	SECRET_KEY= "17@lames.com" #os.environ.get("SECRET_KEY") or "17@lames.com"
	SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
	'sqlite:///' + os.path.join(basedir,'app.db')
DEBUG = True
PORT = 1234