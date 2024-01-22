from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

from flask_jwt_extended import JWTManager, create_access_token
from models import User
from database import db
from werkzeug.security import generate_password_hash, check_password_hash

from flask_migrate import Migrate

# Load environment variables from .env file
load_dotenv()

path = os.getcwd()
parent = os.path.dirname(path)

# app = Flask(__name__, template_folder=parent + '/frontend/public')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
print(app.config['SQLALCHEMY_DATABASE_URI'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

db.init_app(app)
jwt = JWTManager(app)

migrate = Migrate(app, db)

@app.route('/')
def home():
    # just say hello world
    return 'Hello !!!!'


@app.route('/signup', methods=['POST'])
def signup():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username is None or password is None:
        return jsonify({"msg": "Missing username or password"}), 400

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({"msg": "Username already exists"}), 400

    user = User(username=username)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"msg": "Signup successful", "user": user.username}), 201


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    user = User.query.filter_by(username=username).first()

    if user is None or not user.check_password(password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)



@app.errorhandler(404)
def page_not_found(e):
    # your custom response here
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": "Bad request"}), 400

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error"}), 500


# This part is for running the app
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=3002)
