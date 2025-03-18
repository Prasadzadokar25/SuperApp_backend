from src.sign_up.controller.controller import SignUpController
from src.login.controller.login_controller import LoginController
from flask import Blueprint

prasad_blueprint = Blueprint('login', __name__)

prasad_blueprint.add_url_rule('/login', view_func=LoginController.checkLoginCredential, methods=['POST'])
prasad_blueprint.add_url_rule('/checkMobileStatus/<number>', view_func=SignUpController.checkMobileNumberStatus, methods=['GET'])
prasad_blueprint.add_url_rule('/isReferenceCodeValid/<code>', view_func=SignUpController.isReferenceCodeValid, methods=['GET'])
prasad_blueprint.add_url_rule('/signUpWithGoogle', view_func=SignUpController.signUpWithGoogle, methods=['POST'])
