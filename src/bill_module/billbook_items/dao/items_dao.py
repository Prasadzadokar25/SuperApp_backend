
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


