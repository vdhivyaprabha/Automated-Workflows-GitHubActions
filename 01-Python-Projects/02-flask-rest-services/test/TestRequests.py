import requests

url_instance = "http://127.0.0.1:5000/"
response_content = requests.get(url=url_instance)
print(response_content.text)