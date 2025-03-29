from src.bill_module.billbook_items.controller.items_controller import ItemsController
from src.bill_module.shop_manegment.controller.shop_registration_controller import ShopRegistrationContoller
from src.sign_up.controller.controller import SignUpController
from src.login.controller.login_controller import LoginController
from src.user_manegment.controller.user_manegment_controller import UserManegmentController
from flask import Blueprint


prasad_blueprint = Blueprint('login', __name__)

prasad_blueprint.add_url_rule('/login', view_func=LoginController.checkLoginCredential, methods=['POST'])
prasad_blueprint.add_url_rule('/checkMobileStatus/<number>', view_func=SignUpController.checkMobileNumberStatus, methods=['GET'])
prasad_blueprint.add_url_rule('/isReferenceCodeValid/<code>', view_func=SignUpController.isReferenceCodeValid, methods=['GET'])
prasad_blueprint.add_url_rule('/signUpWithGoogle', view_func=SignUpController.signUpWithGoogle, methods=['POST'])

user_manegment_blueprint = Blueprint('user_manegment',__name__)
user_manegment_blueprint.add_url_rule('/user/<user_id>', view_func=UserManegmentController.getUserInfo, methods=['GET'])

shop_manegment_blueprint = Blueprint('shop_manegment',__name__)
shop_manegment_blueprint.add_url_rule("/register_shop",view_func=ShopRegistrationContoller.registerNewShop, methods=['POST'])
shop_manegment_blueprint.add_url_rule("/checkShopRegistry/<user_id>",view_func=ShopRegistrationContoller.checkShopRegistry, methods=['GET'])
shop_manegment_blueprint.add_url_rule("/billbookshop/<shop_id>",view_func=ShopRegistrationContoller.getShopInfo, methods=['GET'])

item_manegment_blueprint = Blueprint('item_manegment',__name__)
item_manegment_blueprint.add_url_rule("/addnewbillbookitem",view_func=ItemsController.add_item,methods=['POST'])