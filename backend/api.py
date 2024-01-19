from flask import Flask
import os

path = os.getcwd()
parent = os.path.dirname(path)

app = Flask(__name__, template_folder=parent + '/frontend')


@app.route('/')
def home():
    return {}

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=3002)
