from flask import request, jsonify
from login.dao.login_dao import LoginDao

class LoginController:

    @staticmethod
    def checkLoginCredential():
        """
        Handles login requests by validating input and authenticating the user.

        Returns:
        - 200 OK with user_id if login is successful.
        - 400 Bad Request if username or password is missing.
        - 401 Unauthorized if credentials are invalid.
        - 500 Internal Server Error if a database error occurs.
        """
        try:
            data = request.get_json()
            if not data or "username" not in data or "password" not in data:
                return jsonify({"error": "Missing username or password"}), 400
            
            username = data["username"]
            password = data["password"]
            
            user_id = LoginDao().checkLoginCredential(username, password)  

            if user_id:
                return jsonify({"message": "Login successful", "user_id": user_id}), 200
            else:
                return jsonify({"error": "Invalid credentials"}), 401

        except Exception as e:
            print(f"Server error: {e}")  # Log the error for debugging
            return jsonify({"error": "Internal server error"}), 500
