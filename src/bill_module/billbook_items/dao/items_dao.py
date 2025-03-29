
from src.bill_module.billbook_items.model.items_model import BillbookItem
from src.db_config import DbConfig
from flask import jsonify


class BillbookItemsDao:

    def get_items(self,shop_id):
        """
        Fetches all items associated with a given shop_id.
        
        Parameters:
        shop_id (int): The ID of the shop whose items need to be retrieved.
        
        Returns:
        JSON response containing item data and HTTP status code.
        """

        query='''select * from billbook_items where shop_id=%s'''

        try:

            connection=DbConfig().get_db_connection()
            cursur=connection.cursor()
            cursur.execute(query,(shop_id))
            result=cursur.fetchall()
            return result
        except Exception as e:
            raise Exception(str(e))
        finally:
            cursur.close()

    def add_stock_items(self,item_id,billbook_item:BillbookItem):
        """
        Updates stock quantity of a specific item in the database.
        
        Parameters:
        item_id (int): The ID of the item whose stock needs to be updated.
        billbook_item (BillbookItem): Object containing updated stock information.
        
        Returns:
        JSON response indicating success or failure.
        """

        query='''update billbook_items set item_stock=%s where item_id=%s '''
        try:
            connection=DbConfig().get_db_connection()
            cursur=connection.cursor()
            cursur.execute(query,(billbook_item.item_stock,item_id))
            connection.commit()
            return True
        except Exception as e:
            raise Exception (str(e)) 
        finally:
            cursur.close()


    def add_new_item(self,item:BillbookItem):
        """
        Inserts a new item (party) into the database.
        
    
        """
        query='''insert into billbook_items (item_name,item_unit,item_sale_price,item_purchase_price,item_gst,item_shn_no,item_stock,item_image,item_description,item_low_stock_alert,item_low_stock_quantity,shop_id) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        query2 = "select item_id from billbook_items where item_name =%s and shop_id = %s"
        try:
            connection=DbConfig().get_db_connection()
            cursur=connection.cursor()
            cursur.execute(query2,(item.item_name, item.shop_id))
            result=cursur.fetchall()
            if result:
                return jsonify({"message":"item with this name already exists"}),209
            cursur.execute(query,(item.item_name,item.item_unit,item.item_sale_price,item.item_purchase_price,item.item_gst,item.item_shn_no,item.item_stock,item.item_image,item.item_description,item.item_low_stock_alert,item.item_low_stock_quantity, item.shop_id))
            connection.commit()
            return jsonify({"message":"item added sucessfully!"}),200       
        except Exception as e:
            connection.rollback()  # Rollback to prevent auto-increment issue

            return jsonify({f"message":f"server error{e}"}),400
        finally:
            cursur.close()