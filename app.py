from db import *
from flask_jwt import JWT
from resource.categories import AllCategory, Category
from resource.pets import AllPets, Pets
from security import authenticate , identity
from resource.user import AllUser, User

jwt = JWT(app,authenticate,identity)

api.add_resource(User, "/user")
api.add_resource(AllUser, "/allusers")
api.add_resource(Category, "/category")
api.add_resource(AllCategory, "/allcategory")
api.add_resource(Pets, "/pet")
api.add_resource(AllPets, "/allpets")


if __name__ == "__main__":
    app.run(debug=True , port=5000)
    
