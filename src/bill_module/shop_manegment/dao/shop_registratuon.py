from flask import jsonify
from src.db_config import DbConfig


class ShopRegistrationDao :
    
        def registerShop(self,data):
            query='''insert into billbook_shops (shop_name,shop_gstin,shop_pan,shop_address,user_id) values(%s,%s,%s,%s,%s)'''
            try:
                connection=DbConfig().get_db_connection()
                cursur=connection.cursor()
        
                cursur.execute(query,(data['shop_name'],data['shop_gstin'],data['shop_pan'],data['shop_address'],data['user_id'],))
                connection.commit()
                return jsonify({'status':'sucessful', "message":"shop register succefuly"}),200       
            except Exception as e:
                return jsonify({'status':'failed',"message":str(e)}),400
            finally:
                cursur.close()
                
        def checkShopRegistry(self,user_id):
            query = f"select * from billbook_shops where user_id = {user_id}"
            try:
                connection=DbConfig().get_db_connection()
                cursur=connection.cursor()
                cursur.execute(query)
                data = cursur.fetchall()
               
                return jsonify({'status':'true','data':data}),200
            except Exception as e:
                print(e)
                return jsonify({"status":"false","error":f"internal server error{e}"}),400