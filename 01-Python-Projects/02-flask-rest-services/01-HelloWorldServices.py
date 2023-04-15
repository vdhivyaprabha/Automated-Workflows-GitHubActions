from flask import Flask
from flask_restful import Resource, Api

flask_app_instance = Flask(__name__)
flask_api_instance = Api(flask_app_instance)

class Helloworld(Resource):
  
  def __init__(self):
    pass

  def get(self):
    return {"mesage": "Hellow World !!!"}

flask_api_instance.add_resource(Helloworld, '/')

if __name__ == '__main__':
  flask_app_instance.run(debug=True)