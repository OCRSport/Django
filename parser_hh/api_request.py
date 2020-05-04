import requests
import pprint

response = requests.get('http://185.20.224.130/skills/skills/')

pprint.pprint(response.json())