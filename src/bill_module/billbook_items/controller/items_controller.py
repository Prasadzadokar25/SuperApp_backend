
from flask import request,jsonify

from src.bill_module.billbook_items.model.items_model import BillbookItem
from src.bill_module.billbook_items.dao.items_dao import BillbookItemsDao


class ItemsController:
    def get_items(shop_id):
        """
        Controller method to get items for a specific shop.
        """
        try:
            data= BillbookItemsDao().get_items(shop_id)
            return jsonify({'data': data}), 200
        except Exception as e:
            return jsonify({'message': str(e)}), 400

    def add_items(item_id):
        """
        Controller method to update the stock of an item.
        """
        try:

            data=request.json
            items=BillbookItem.from_json(data)
            sucess= BillbookItemsDao().add_stock_items(item_id, items) 
            if sucess:
                return jsonify({"message":"Item Stock updated successfully"}),200
            else:
                return jsonify({"message":"Failed to update stock"}),500
            
        except Exception as e:
            return jsonify({"message":str(e)}),400
            