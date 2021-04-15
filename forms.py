from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class loginForm(FlaskForm):
	username = StringField("username", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])
	rememmber_me = BooleanField("rememmber_me")
	amine = SubmitField("Sing on")