# from src.db_config import get_db_connection
from src.db_config import DbConfig
from werkzeug.security import generate_password_hash, check_password_hash
from src.sign_up.model.model import User
from flask import jsonify

class SignUpDao:

    def register_user(self,user:User):
        query2='''select * from users where user_contact=%s or user_email=%s '''    
        query='''insert into users (user_name,password,user_contact,user_email) values(%s,%s,%s,%s) '''
        try:
                connection=DbConfig().get_db_connection()
                cursur=connection.cursor()
                cursur.execute(query2,(user.user_contact,user.user_email)) 
                result=cursur.fetchall()
                if result:
                     return jsonify({"massage":"user already exist"}),209
                print(f"Type of user.password: {type(user.password)}")

                hashed_password=generate_password_hash(user.password)
                print(hashed_password)

                cursur.execute(query,(user.user_name,hashed_password,user.user_contact,user.user_email))
                connection.commit()
                return jsonify({"massage":"user register succefully"}),200
        except Exception as e :    
            return         jsonify({f"massage":str(e)}),400

        finally:
             connection.close
             cursur.close

