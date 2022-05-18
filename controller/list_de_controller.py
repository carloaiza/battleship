from service.list_de_service import ListDEService
from flask import json, Response,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder
from model.ship import Ship
from jwt import encode, decode, exceptions
from os import getenv
import time

expire_token = int(time.time())


app_list_de = Blueprint('app_list_de',__name__)
list_de_service = ListDEService()


@app_list_de.route('/listde')
def list():
    token = None
    if 'x-access-token' in request.headers:
        token = request.headers['x-access-token']
        # return 401 if token is not passed
    if not token:
        return jsonify({'message': 'Token is missing !!'}), 401
    response=validate_token(token)
    if not response:
        return Response(status=200,mimetype="application/json",
                    response=json.dumps(list_de_service.list(),cls=UtilEncoder))
    else:
        return response

@app_list_de.route('/listde',methods=['POST'])
def create():
    data = request.json
    return list_de_service.add(Ship(data,list_de_service.list_de.count +1))

@app_list_de.route('/login',methods=['POST'])
def login():
    data = request.json
    return token(data)

def token(data):
    llave = "HolaLindos"#getenv('secret')
    token = encode(payload={**data,"duration":expire_token},key=llave,algorithm="HS256")
    return token.encode("UTF-8")

def validate_token(token):
    try:
        decode(token,"HolaLindos","HS256")
    except exceptions.DecodeError:
        return {"message":"Token inválido"}
    except exceptions.ExpiredSignatureError:
        return {"message":"Token vencido"}