from flask import Flask , render_template

app1 = Flask(__name__)

@app1.route("/")
def home():
	user={"username":"amine"}
	return render_template('index.html',user=user, title = "Home Page")

if __name__ == '__main__':
	app1.run()