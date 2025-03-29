from flask import jsonify
from src.db_config import DbConfig


class UserManegmentDao:
    
    def getUserInfo(self,user_id):
        query_check = '''SELECT * FROM users WHERE user_id = %s OR user_email = %s'''    
        
        try:
            connection = DbConfig().get_db_connection()
            cursor = connection.cursor()

            # Check if user already exists
            cursor.execute(query_check, (user_id,user_id))
            data = cursor.fetchone()

            if user_id:
                return jsonify({"status":"success", "data": data}), 200

            return jsonify({"status": "failed", "message": "No user found"}), 404

        except Exception as e:
            return jsonify({"message": str(e)}), 400

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
