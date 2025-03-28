

from config import app

@app.route('/')
def home():
    return "Flask heroku app."

if __name__ == '__main__':
    app.run()