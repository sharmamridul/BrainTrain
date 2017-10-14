from flask import Flask, render_template, flash
from flask.ext.bootstrap import Bootstrap

app = Flask('__name__')

@app.route("/")
def hello():
	return render_template('index.html')

if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 8000, debug = True)
