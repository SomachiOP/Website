from rich.traceback import install; install()
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html"), 200
#Bruh Momento
if __name__ == "__main__":
	app.run(debug=True)
