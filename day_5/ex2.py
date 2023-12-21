from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Someone'

@app.route('/fruit/<int:name>')
def fruit(name):
    return f"You said {name}"

