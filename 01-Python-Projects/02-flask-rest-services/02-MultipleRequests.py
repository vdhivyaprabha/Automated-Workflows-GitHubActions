from flask import Flask
from flask_restful import Resource, Api
import json
import random
import string

flask_app_instance = Flask(__name__)
flask_api_instance = Api(flask_app_instance)
people_dictionary = {}

"""
  This class is intended to create a simple rest service using flask with get post and delete methods.
  build and deploy the service using Git hub actions.

  Using GET To - gets the list of all names inserted as part of the dictionary.
  Using POST To - Insert a new name to the people dictionary.
  Using DELETE To - Delete name from the people dictionary using the key.
"""
class People(Resource):

  def get(self):
    return json.dumps(people_dictionary, indent = 4)
	
  def post(self, name_tobe_inserted):
    response_dict = {}
    #TODO check if the key is already present in the dictionary and create keys until we get new keys.
    key_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    people_dictionary[key_name] = name_tobe_inserted
    response_dict["content-added"] = key_name
    response_dict["message"] = "The entry is successfully added to the database."
    return json.dumps(response_dict, indent = 4)
	
  def delete(self,key_tobe_deleted):
    response_dict = {}
    for element_key in people_dictionary:
      if element_key == key_tobe_deleted:
        del people_dictionary[element_key]
        response_dict["content-removed"] = element_key
        response_dict["message"] = "The entry is successfully deleted from the database."
        break
    return json.dumps(response_dict, indent = 4)
			
flask_api_instance.add_resource(People, '/Name')

if __name__ == '__main__':
  flask_app_instance.run(debug=True)