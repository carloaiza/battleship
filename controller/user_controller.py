from flask import json, Response,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder
from service.user_service import UserService

app_user = Blueprint("app_user",__name__)
user_service = UserService()

@app_user.route("/user")
def get_users():
    return Response(status=200,mimetype="application/json",
                    response=json.dumps(user_service.get_users(),cls=UtilEncoder))

