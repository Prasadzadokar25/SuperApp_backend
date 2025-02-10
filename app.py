from flask import Flask, jsonify
from src.billbook_items.controller.items_controller import ItemsController
from src.parties.controller.parties_controller import PartiesController
from src.sign_up.controller.controller import SignUpController

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Flask app connected to MySQL!"

app.add_url_rule('/register_user',view_func=SignUpController.signUp, methods=['POST'])
app.add_url_rule('/get_parties/<int:shop_id>',view_func=PartiesController.getParties,methods=['GET'])
app.add_url_rule('/create_party',view_func=PartiesController.createParty,methods=['POST'])
app.add_url_rule('/get_items/<int:shop_id>',view_func=ItemsController.get_items,methods=['GET'])
app.add_url_rule('/add_stock/<int:item_id>',view_func=ItemsController.add_items,methods=['PUT'])

if __name__ == '__main__':
    # app.run(debug=True) #start running the server
    app.run(host='0.0.0.0', port=5000)