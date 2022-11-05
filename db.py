# from flask import Flask
# from flask_restful import Api
# from flask_sqlalchemy import SQLAlchemy
# import os


# app = Flask(__name__)


# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.secret_key = "She_didn't_love_U"
# api = Api(app)

# db = SQLAlchemy(app)


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
