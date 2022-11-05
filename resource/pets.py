from models.pets import PetModel
from flask_restful import Resource,reqparse

from models.user import UserModel
from models.categories import CategoryModel
# from flask_jwt import jwt_required

class Pets(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'id',
        type = int,
        required = True,
        help = "Pet ID cannot be blank"
    )
    parser.add_argument(
        'pet_name',
        type = str,
        required = True,
        help = "Pet name cannot be blank"
    )
    parser.add_argument(
        'price',
        type = float,
        required = True,
        help = "Price cannot be blank"
    )
    parser.add_argument(
        'info',
        type = str,
        required = True,
        help = "Pet Info cannot be blank"
    )
    parser.add_argument(
        'img_url',
        type = str,
        required = True,
        help = "Pet Url cannot be blank"
    )
    parser.add_argument(
        'seller_id',
        type = int,
        required = True,
        help = "Seller ID cannot be blank"
    )
    parser.add_argument(
        'category_id',
        type = int,
        required = True,
        help = "Category ID cannot be blank"
    )
    
    # @jwt_required()
    def post(self):
        data = Pets.parser.parse_args()
        pet = PetModel.find_pet_by_id(data['id'])
        
        if pet:
            return {'Massage' : "Pet with this ID {} is already exists!".format(data['id'])} , 400
        
        user = UserModel.find_by_id(data['seller_id'])
        
        if user is None:
            return {'Massage' : "Seller with this ID {} doesn't exists!".format(data['seller_id'])} , 400
        else:
            if user.usertype != 'seller':
                return {'Massage' : "{} is not a seller".format(data['seller_id'])} , 400
            
        catego = CategoryModel.find_catego_by_id(data['category_id'])
        
        if catego is None:
            return {'Massage' : "Category with this ID {} doesn't exists!".format(data['seller_id'])} , 400
        
        pet = PetModel(**data)
        
        try:
            pet.save_to_db()
        except:
            return {'Massage' : "An error occured while inserting to database"}, 500
        
        return pet.json(), 201
    
    # @jwt_required()
    def delete(self):
        data = Pets.parser.parse_args()
        user = PetModel.find_pet_by_id(data["id"])
        if user:
            user.delete_from_db()
            return {"Massage" : "{} has been deleted".format(data["id"])}, 200
        
        return {"Massage" : "An error occurs while deleting pets"}, 500
    
    # @jwt_required()
    def put(self):
        data = Pets.parser.parse_args()
        pet = PetModel.find_pet_by_id(data["id"])
        
        if pet is None:
            pet = PetModel(**data)
        else:
            pet.id = data["id"]
            pet.pet_name = data["pet_name"]
            pet.price = data['price']
            pet.info = data['info']
            pet.img_url = data['img_url']
            pet.seller_id = data['seller_id']
            pet.category_id = data['category_id']
        
        pet.save_to_db()
        
        return pet.json(), 200
    
class AllPets(Resource):
    def get(self):
        pets = PetModel.query.all()
        return {"All Pets" : [user.json() for user in pets]}