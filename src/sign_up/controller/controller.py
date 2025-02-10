from flask import request

from src.sign_up.dao.dao import SignUpDao
from src.sign_up.model.model import User
class SignUpController:

    @staticmethod
    def signUp(): 
        data=request.json 
        user = User().from_json(data)
        return SignUpDao().register_user(user)



