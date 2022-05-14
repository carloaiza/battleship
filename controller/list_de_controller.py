from service.list_de_service import ListDEService
from flask import json, Response,jsonify,Blueprint, request
from util.util_encoder import UtilEncoder

app_list_de = Blueprint('app_list_de',__name__)
list_de_service = ListDEService()

@app_list_de.route('/listde')
def list():
    return Response(status=200,mimetype="application/json",
                    response=json.dumps(list_de_service.list(),cls=UtilEncoder))