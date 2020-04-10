from werkzeug.security import safe_str_cmp
from models.users import UserModel


def authenticate(username, password):
    user = UserModel.find_user_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identify(payload):
    user_id = payload['identity']
    return UserModel.find_user_by_user_id(user_id)
