from resource.categories import AllCategory, Category
from resource.pets import AllPets, Pets
from resource.user import AllUser, User
from flask import Flask
from flask_restful import Api
import os

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://thunyaung:@localhost/pet_shop'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
try:
    prodURI = os.getenv("DATABASE_URL")
    prodURI = prodURI.replace("postgres://", "postgresql://")
    app.config['SQLALCHEMY_DATABASE_URI'] = prodURI
except:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Zawnay2001@localhost/petshop'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "She-didn't-love-U"
api = Api(app)


api.add_resource(User, "/user")
api.add_resource(AllUser, "/allusers")
api.add_resource(Category, "/category")
api.add_resource(AllCategory, "/allcategory")
api.add_resource(Pets, "/pet")
api.add_resource(AllPets, "/allpets")


if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True , port=5000)
    
