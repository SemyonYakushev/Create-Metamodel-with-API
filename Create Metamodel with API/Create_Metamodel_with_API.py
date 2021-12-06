from xml.etree import ElementTree
import requests
import base64
import json
import urllib3
import sys
import pandas as pd

auth_key = 'c3lzdGVtIGFkbWluaXN0cmF0b3I6MTIzcXdlQVNEKw=='
base_url = 'http://185.53.22.117:8008'
file = "export.xlsx"


objects = pd.read_excel(io=file, header = 0, engine='openpyxl', squeeze = True)
print(objects)

list_types = []

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json', 
    'Authorization': 'Basic ' + auth_key,
}

for items in objects:
   list_types.append({'Name': items})
   
for type in list_types:
   jdata = json.dumps(type)
   response = requests.post(base_url + '/api/metaModel/objectType', headers=headers, data=jdata)

#class APIGET:
    #def get_objecttypes(self, auth_key, base_url):
       #pass

    #def get_relationshipstypes(self, auth_key, base_ur):
        #pass

    #def get_relationships_pairs(self, auth_key, base_ur):
        #pass

    #def get_atributestype(self, auth_key, base_ur):
        #pass

    #def get_atributes_assignment(self, auth_key, base_ur):
        #pass
