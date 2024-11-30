from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World - from Python and Flask hosted at Vercel'

@app.route('/about')
def about():
    return 'Last updated: 30-11-2024 - A Python and Flask Web App'