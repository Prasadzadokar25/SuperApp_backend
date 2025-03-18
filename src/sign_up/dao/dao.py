# from src.db_config import get_db_connection
from src.db_config import DbConfig
from werkzeug.security import generate_password_hash, check_password_hash
from src.sign_up.model.model import User
from flask import jsonify
import random
import string
def generate_referral_code(length=8):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choices(characters, k=length))

class SignUpDao:
    
    
    def register_user(self,user:User):
        query2='''select * from users where user_contact=%s or google_uid=%s '''    
        query='''insert into users (user_name,password,user_contact,user_email,user_ref_code,login_type,google_uid,referred_by) values(%s,%s,%s,%s,%s,%s,%s,%s) '''
        try:
                connection=DbConfig().get_db_connection()
                cursur=connection.cursor()
                cursur.execute(query2,(user.user_contact,user.user_email)) 
                result=cursur.fetchall()
                if result:
                     return jsonify({"message":"User already exist"}),409

                hashed_password=generate_password_hash(user.password)

                cursur.execute(query,(user.user_name,hashed_password,user.user_contact,user.user_email,generate_referral_code(),user.login_type,user.google_uid,user.refered_by))
                connection.commit()
                return jsonify({"message":"user register succefully"}),200
        except Exception as e :    
            return         jsonify({f"message":str(e)}),400

        finally:
             connection.close
             cursur.close
             
    def register_user_with_google(self, user: User):
        query_check = '''SELECT user_id FROM users WHERE google_uid = %s'''    
        query_insert = '''INSERT INTO users (user_email, user_ref_code, login_type, google_uid) VALUES (%s, %s, %s, %s)'''
        
        try:
            connection = DbConfig().get_db_connection()
            cursor = connection.cursor()

            # Check if user already exists
            cursor.execute(query_check, (user.google_uid,))
            user_id = cursor.fetchone()

            if user_id:
                return jsonify({"user_id":user_id, "note": "This is an existing user"}), 200

            # Register new user
            cursor.execute(query_insert, (user.user_email, generate_referral_code(), user.login_type, user.google_uid))
            user_id = cursor.lastrowid   # Retrieve newly created user_id
            connection.commit()

            return jsonify({"user_id": user_id, "message": "User registered successfully"}), 200

        except Exception as e:
            return jsonify({"message": str(e)}), 400

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()


    def checkMobileNumberStatus(self, number):
        query = f"SELECT user_id FROM users WHERE user_contact = {number}"
        print(number)

        try:
            connection = DbConfig().get_db_connection()
            cursor = connection.cursor()
            cursor.execute(query)  # Ensure it's a tuple
            result = cursor.fetchall()

            cursor.close()  # Close cursor before closing connection
            connection.close()

            return bool(result)  # Return True if number exists, else False

        except Exception as e:
            print(f"Server Error: {e}")  # Log actual error
            raise Exception("Server error")
        
    def isReferenceCodeValid(self, code):
        query = f"SELECT user_id FROM users WHERE user_ref_code = '{code}'"

        try:
            connection = DbConfig().get_db_connection()
            cursor = connection.cursor()
            cursor.execute(query)  # Ensure it's a tuple
            result = cursor.fetchone()

            cursor.close()  # Close cursor before closing connection
            connection.close()

            if result:
                return {
                "isValid":bool(result),
                "refered_user_id":result['user_id']
                }   # Return True if number exists, else False
            else :
                return {
                  "isValid":bool(result)  
                }

        except Exception as e:
            print(f"Server Error: {e}")  # Log actual error
            raise Exception("Server error")

            
                
                
