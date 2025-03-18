from flask import request

from src.bill_module.parties.dao.parties_dao import PartiesDao

from src.bill_module.parties.model.parties_model import BillbookCustomerInfo

class PartiesController:
    def getParties(shop_id):
        return PartiesDao().get_parties(shop_id)
    
    def createParty():
        data=request.json
        customer=BillbookCustomerInfo().from_json(data)
        return PartiesDao().create_party(customer)

