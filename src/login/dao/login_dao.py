from db_config import get_db_connection
from werkzeug.security import check_password_hash

class LoginDao:
    def checkLoginCredential(self, username, password):
        """
        Checks user credentials against the database.

        Returns:
        - user_id if authentication is successful.
        - Raises an exception if a database error occurs.
        """
        query = """SELECT user_id, password FROM users WHERE user_contact = %s OR user_email = %s"""
        connection = None
        cursor = None

        try:
            connection = get_db_connection()
            cursor = connection.cursor()  # Ensures result is a dictionary

            cursor.execute(query, (username, username))
            result = cursor.fetchone()
            
            if result:
                user_id = result['user_id']
                indbpassword = result['password']
                
                if check_password_hash(indbpassword, password):
                    return user_id  # Return user_id if login is successful
                
            return None  # Return None if login fails

        except Exception as e:
            print(f"Database error: {e}")  # Log error for debugging
            raise Exception("Database connection error")  # Raise an exception

        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
