from flask import Flask, request, jsonify

from src.bill_module.bills.dao.bills_dao import BillDao

class BillController:
    
    def get_bill_for_dates(shop_id,start_date,end_date):
        try:
            bills =  BillDao().get_bill_for_dates(shop_id,start_date,end_date)
            if bills:
                return jsonify({"data":bills}),200
            return jsonify({"massage":"No data found!"}),204
        except Exception as e:
            return jsonify({"error":"server internal error"}),500