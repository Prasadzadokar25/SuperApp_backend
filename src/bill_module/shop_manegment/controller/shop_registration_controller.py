from flask import request
from src.bill_module.shop_manegment.dao.shop_registratuon import ShopRegistrationDao


class ShopRegistrationContoller:
    
    @staticmethod
    def registerNewShop():
        data = request.get_json()
        return ShopRegistrationDao().registerShop(data)
    
    @staticmethod
    def checkShopRegistry(user_id):
        return ShopRegistrationDao().checkShopRegistry(user_id)
    
    @staticmethod
    def getShopInfo(shop_id):
        return ShopRegistrationDao().getShopInfo(shop_id)
        
        