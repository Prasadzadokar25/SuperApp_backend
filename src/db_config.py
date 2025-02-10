from flask import Flask, jsonify
import pymysql.cursors

# Initialize the Flask app
app = Flask(__name__)

# Database connection configuration
def get_db_connection():
    connection = pymysql.connect(
        host='localhost', 
        user='root',           # Your MySQL username
        password='##Prasad25',   # Your MySQL password
        database='superapp_db',    # Your MySQL database name
        cursorclass=pymysql.cursors.DictCursor  # To get results as dictionaries
    )
    return connection