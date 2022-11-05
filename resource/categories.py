from models.categories import CategoryModel
from flask_restful import Resource,reqparse
# from flask_jwt import jwt_required

class Category(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'id',
        type = int,
        required = True,
        help = "Category ID cannot be blank"
    )
    parser.add_argument(
        'category_name',
        type = str,
        required = True,
        help = "category name cannot be blank"
    )
    

    # @jwt_required()
    def post(self):
        data = Category.parser.parse_args()
        user = CategoryModel.find_catego_by_id(data['id'])
        catego = CategoryModel.find_catego_by_name(data['category_name'])
        
        if user:
            return {"Massage" : "PetCategory with This ID {} is already existed!".format(data["id"])} , 400
        
        if catego:
            return {"Massage" : "PetCategory with This Categoryname {} is already existed!".format(data["category_name"])}, 400
        
        user = CategoryModel(**data)
        
        try:
            user.save_to_db()
        except:
            return {'Massage' : "An error occured while inserting to database"}, 500
        
        return {"Massage" : "PetCategory created successfully"}, 200
    
    # @jwt_required()
    def delete(self):
        data = Category.parser.parse_args()
        user = CategoryModel.find_catego_by_id(data["id"])
        if user:
            user.delete_from_db()
            return {"Massage" : "{} has been deleted".format(data["id"])}, 200
        
        return {"Massage" : "An error occurs while deleting user"}, 500
    
    # @jwt_required()
    def put(self):
        data = Category.parser.parse_args()
        catego = CategoryModel.find_catego_by_id(data["id"])
        
        if catego is None:
            catego = CategoryModel(**data)
        else:
            catego.id = data["id"]
            catego.category_name = data["username"]
        
        catego.save_to_db()
        
        return catego.json(), 200
    
class AllCategory(Resource):
    def get(self):
        categories = CategoryModel.query.all()
        return {"All Category" : [catego.json() for catego in categories]}