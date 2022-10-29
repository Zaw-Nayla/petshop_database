from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Zawnay2001@localhost/petshop'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "She_didn't_love_U"
api = Api(app)


db = SQLAlchemy(app)