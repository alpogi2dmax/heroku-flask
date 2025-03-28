from flask import Flask

from config import app

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask heroku app."

if __name__ == '__main__':
    app.run()