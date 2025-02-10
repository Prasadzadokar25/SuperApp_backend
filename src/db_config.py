import pymysql
class DbConfig:
# Initialize the Flask app

# Database connection configuration

    def get_db_connection(self):
        self.connection = pymysql.connect(
        host='192.168.0.105', 
        user='pratik',           # Your MySQL username
        password='Pratik@999',   # Your MySQL password
        database='superapp_db',    # Your MySQL database name
        cursorclass=pymysql.cursors.DictCursor  # To get results as dictionaries
         )
        self.connection.autocommit=True 
        return self.connection
