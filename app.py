from flask import Flask, render_template

app = Flask(__name__)

name = 'wuxin'
Items = {'name':'wuxin', 'age':18 }

@app.route('/')
def index():
	return render_template('index.html', name = name, Items = Items)
