from models.user import UserModel
from flask_restful import Resource,reqparse

class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'id',
        type = int,
        required = True,
        help = "User ID cannot be blank"
    )
    parser.add_argument(
        'username',
        type = str,
        required = True,
        help = "username cannot be blank"
    )
    parser.add_argument(
        'password',
        type = str,
        required = True,
        help = "password cannot be blank"
    )
    parser.add_argument(
        'usertype',
        type = str,
        required = True,
        help = "usertype cannot be blank"
    )

    
    def post(self):
        data = User.parser.parse_args()
        user = UserModel.find_by_id(data['id'])
        
        if user:
            return {"Massage" : "User whith This ID {} is already existed !".format(data["id"])} , 400
        
        if data['usertype'] == "seller" or data['usertype'] == "buyer":
            user = UserModel(**data)
            try:
                user.save_to_db()
            except:
                return {'Massage' : "An error occured while inserting to database"}, 500
            
            return {"Massage" : "user created successfully"}, 200
        
        return {"Massage" : " {} Usertype is not supported!".format(data["usertype"])} , 400
    
    def delete(self):
        data = User.parser.parse_args()
        user = UserModel.find_by_id(data["id"])
        if user:
            user.delete_from_db()
            return {"Massage" : "{} has been deleted".format(data["id"])}, 200
        
        return {"Massage" : "An error occurs while deleting user"}, 500
    
    def put(self):
        data = User.parser.parse_args()
        user = UserModel.find_by_id(data["id"])
        
        if user is None:
            user = UserModel(data["id"],data["username"],data["password"],data["usertype"])
        else:
            user.id = data["id"]
            user.username = data["username"]
            user.password = data["password"]
            user.usertype = data["usertype"]
        
        user.save_to_db()
        
        return user.json(), 200
    
class AllUser(Resource):
    def get(self):
        users = UserModel.query.all()
        return {"All users" : [user.json() for user in users]}