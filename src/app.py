# from flask import Flask
# from bills.controller.bills_controller import BillController
# from login.controller.login_controller import LoginController



# # Initialize Flask App
# app = Flask(__name__)


# app.add_url_rule('/login', view_func=LoginController.checkLoginCredential, methods=['POST'])
# app.add_url_rule('/get_bill_for_dates/<int:shop_id>/<start_date>/<end_date>', view_func=BillController.get_bill_for_dates, methods=['GET'])


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)