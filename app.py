from flask import Flask, request, jsonify
from controllers.controllers import router
from flask_restful import Api, Resource
from controllers.controllers import Search


app = Flask(__name__)
api = Api(app)
app.register_blueprint(router)

# regiser resource
api.add_resource(Search, '/search')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
