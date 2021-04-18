from app3 import db

class amine(db, Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(128))
	email = db.Column(db.Integer, default=0)