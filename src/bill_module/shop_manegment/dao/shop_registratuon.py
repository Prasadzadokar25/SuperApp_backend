from flask import jsonify
from src.db_config import DbConfig

class ShopRegistrationDao:

    def registerShop(self, data):
        query = '''INSERT INTO billbook_shops (shop_name, shop_gstin, shop_pan, shop_address, user_id) 
                   VALUES (%s, %s, %s, %s, %s)'''
        try:
            connection = DbConfig().get_db_connection()
            cursor = connection.cursor()

            cursor.execute(query, (data['shop_name'], data['shop_gstin'], data['shop_pan'], data['shop_address'], data['user_id']))
            connection.commit()
            cursor.execute("SELECT LAST_INSERT_ID()")  # Fetch the last inserted ID
            shop_id = cursor.fetchall() [0] 
            
            return jsonify({'status': 'successful', "message": "Shop registered successfully", "shop_id": shop_id}), 200
        except Exception as e:
            print(e)
            return jsonify({'status': 'failed', "message": str(e)}), 400
        finally:
            cursor.close()
            connection.close()

    def checkShopRegistry(self, user_id):
        query = "SELECT shop_id FROM billbook_shops WHERE user_id = %s"
        try:
            connection = DbConfig().get_db_connection()
            cursor = connection.cursor()
            cursor.execute(query, (user_id,))
            data = cursor.fetchall()
            
            if data:
                shop_ids = [] # Extract all shop_ids
                for e in data:
                    shop_ids.append(e["shop_id"])
                print(shop_ids)
                return jsonify({'status': 'true',"massage":"data fetch succefully", 'shop_ids': shop_ids}), 200
            else:
                return jsonify({'status': 'true', 'massage': "No data found"}), 209
        except Exception as e:
            print(e)
            return jsonify({"status": "false", "error": f"Internal server error: {e}"}), 400
        finally:
            cursor.close()
            connection.close()
