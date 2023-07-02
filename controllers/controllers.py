from flask import Blueprint, request, jsonify, render_template
from flask_restful import Resource
from services.search_on_www import search_on_web

router = Blueprint('bp1', __name__, static_folder='static')


@router.route('/')
@router.route('/home')
def home_controller():
    return render_template('index.html')



class Search(Resource):
    def get(self):
        print('get on search api called.....')
        return {"Topic App": "Goto Use post api to send topic"}

    def post(self):
        print(f'post request recedived with query::::: {request.get_json()}')
        data = request.get_json()['query']
        print(data)
        result = search_on_web(data)
        print(result)
        return result
