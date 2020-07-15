import json
# import turtle
import urllib.request

url ="http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print("There are", result['number'], "people in space")

people = result['people']
for p in people:
    print(p['name'])