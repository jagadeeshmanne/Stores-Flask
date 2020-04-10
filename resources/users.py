from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.users import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field cannot be left blank.'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field cannot be left blank.'
                        )

    def post(self):
        user_data = UserRegister.parser.parse_args()
        if UserModel.find_user_by_username(user_data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**user_data)
        user.save_to_db()
        return {"message": "User created successfully."}, 201


class User(Resource):
    @jwt_required()
    def get(self, name):
        user = UserModel.find_user_by_username(name)
        if user:
            return user.json(), 200
        return {'message': 'user not exists'}, 404

