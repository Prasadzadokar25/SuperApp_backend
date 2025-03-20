from flask import Flask, jsonify
from flask_cors import CORS
from src.bill_module.bills.controller.bills_controller import BillController
from src.login.controller.login_controller import LoginController
from src.bill_module.billbook_items.controller.items_controller import ItemsController
from src.bill_module.parties.controller.parties_controller import PartiesController
from src.sign_up.controller.controller import SignUpController
from rougth.prasad_rougth import prasad_blueprint
from rougth.prasad_rougth import shop_manegment_blueprint
from rougth.prasad_rougth import user_manegment_blueprint

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Allows all domains by default


@app.route('/')
def home():
    return "Flask app connected to MySQL!"

app.add_url_rule('/register_user',view_func=SignUpController.signUp, methods=['POST'])
app.add_url_rule('/get_parties/<int:shop_id>',view_func=PartiesController.getParties,methods=['GET'])
app.add_url_rule('/create_party',view_func=PartiesController.createParty,methods=['POST'])
app.add_url_rule('/get_items/<int:shop_id>',view_func=ItemsController.get_items,methods=['GET'])
app.add_url_rule('/update_item_stack/<int:item_id>',view_func=ItemsController.update_item_stack,methods=['PUT'])
# app.add_url_rule('/login',view_func=LoginController.checkLoginCredential, methods=['POST'])
app.add_url_rule('/login', view_func=LoginController.checkLoginCredential, methods=['POST'])
app.add_url_rule('/get_bill_for_dates/<int:shop_id>/<start_date>/<end_date>', view_func=BillController.get_bill_for_dates, methods=['GET'])

app.register_blueprint(prasad_blueprint)  # Now login route will work
app.register_blueprint(shop_manegment_blueprint)  # Now login route will work
app.register_blueprint(user_manegment_blueprint)  # Now login route will work



if __name__ == '__main__':
    # app.run(debug=True) #start running the server
    app.run(host='0.0.0.0', port=5000)