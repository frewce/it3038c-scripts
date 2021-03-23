import json
import requests

r = requests.get("http://localhost:3000/")

data = r.json()

type1 = (data[0]['name'])
type2 = (data[0]['color'])

type3 = (data[1]['name'])
type4 = (data[1]['color'])

type5 = (data[2]['name'])
type6 = (data[2]['color'])

type7 = (data[3]['name'])
type8 = (data[3]['color'])

print(type1 + " is " + type2 + ".")
print(type3 + " is " + type4 + ".")
print(type5 + " is " + type6 + ".")
print(type7 + " is " + type8 + ".")
