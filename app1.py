from flask import Flask , render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import loginForm
app1 = Flask(__name__)
app1.config.from_object('config')
app1.config['SECRET_KEY'] = 'any secret string'

db = SQLAlchemy(app1)
migrate = Migrate(db, app1)

@app1.route("/mess")
def amine():
	return render_template("message.html")


@app1.route("/")
def home():
	user={"username":"amine"}
	posts = [
	{"author":{"username":"Mohamed"}},
	{"author":{"username":"Amine"}},
	{"author":{"username":"Khaled"}},
	]
	return render_template('index.html',user=user, title = "Home Page", posts = posts)
@app1.route('/login', methods=['GET', 'POST'])
def log():
	form=loginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, rememmber_me={}'.format(form.username.data, form.rememmber_me.data))
		return redirect('/mess')
	return render_template("login.html", title="Log In", form = form)


if __name__ == '__main__':
	app1.run(port = app1.config["PORT"], debug = app1.config["DEBUG"])