from flask import Flask
from controller.list_de_controller import app_list_de
from controller.user_controller import app_user
from flask_jwt_extended import JWTManager
from os import getenv
import datetime

app = Flask(__name__)

JWTManager(app)
app.register_blueprint(app_list_de)
app.register_blueprint(app_user)

app.config["JWT_SECRET_KEY"]=getenv('secret')
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(minutes=2)

if __name__ == '__main__':
    app.run()
