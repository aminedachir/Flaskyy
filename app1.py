from flask import Flask , render_template

app1 = Flask(__name__)
app1.config.from_object('config')

@app1.route("/")
def home():
	user={"username":"amine"}
	posts = [
	{"author":{"username":"Mohamed"}},
	{"author":{"username":"Amine"}},
	{"author":{"username":"Khaled"}},
	]
	return render_template('index.html',user=user, title = "Home Page", posts = posts)

if __name__ == '__main__':
	app1.run(port = app1.config["PORT"], debug = app1.config["DEBUG"])