# from resource.user import UserModel

# def authenticate(username,password):
#     user = UserModel.find_by_name(username)
#     if user and user.password == password:
#         print(user)
#         return user

# def identity(payload):
#     user_id = payload['identity']
#     user = UserModel.find_by_id(user_id)
#     if user.usertype == 'seller':
#         return user
    