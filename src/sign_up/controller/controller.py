from flask import request,jsonify

from src.sign_up.dao.dao import SignUpDao
from src.sign_up.model.model import User
class SignUpController:

    @staticmethod
    def signUp(): 
        data=request.json 
        user = User().from_json(data)
        return SignUpDao().register_user(user)
    
    @staticmethod
    def signUpWithGoogle(): 
        data=request.json 
        user = User().from_json(data)
        return SignUpDao().register_user_with_google(user)

    @staticmethod
    def checkMobileNumberStatus(number):
        try:
            isPresent =  SignUpDao().checkMobileNumberStatus(number)
            if isPresent:
                return jsonify({"status":isPresent,"message":"Mobile number already present"}),409
            else:
                return jsonify({"status":isPresent}),200
        except Exception as e:
            return jsonify({"error":"Server error{e}"}),500
        
    @staticmethod
    def isReferenceCodeValid(code):
        try:
            result =  SignUpDao().isReferenceCodeValid(code)
            if result['isValid']:
                return jsonify({"status":result['isValid'],'refered_user_id': result['refered_user_id'],"message":"reference code is valid"}),200
            else:
                return jsonify({"status":result['isValid'],"message":"reference code is invalid"}),409
        except Exception as e:
            return jsonify({"error":"Server error"}),500
       
    
