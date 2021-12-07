from xml.etree import ElementTree
import requests
import base64
import json
import urllib3
import sys
import pandas as pd

auth_key = 'c3lzdGVtIGFkbWluaXN0cmF0b3I6MTIzcXdlQVNEKw=='
base_url = 'http://185.53.22.117:8009'
file = "Archimate-Metamodel перевод.xlsx"

columns = ['RelationTypeName', 'FromObjectTypeName', 'ToObjectTypeName']
relations = pd.read_excel(io=file, header = 0, engine='openpyxl', sheet_name = "Mapping")
#print(relations[columns])


rel_list_types = []
headers = {
           'Accept': 'application/json',
           'Content-Type': 'application/json', 
           'Authorization': 'Basic ' + auth_key
}

for rows in relations[columns]:
    #a = {'Name': items['RelationTypeName']}
    #rel_list_types.append(a)
    print(rows)

#class APIGET:
    #def get_objecttypes(self, auth_key, base_url):
       #objects = pd.read_excel(io=file, header = 0, engine='openpyxl', sheet_name = "ObjectTypes")
       #obj_list_types = [] 
       #headers = {
           #'Accept': 'application/json',
           #'Content-Type': 'application/json', 
           #'Authorization': 'Basic ' + auth_key
           #}
       #for rows in objects:
           #obj_list_types.append({'Name': rows})
           #for type in obj_list_types:
               #jdata = json.dumps(type)
               #response = requests.post(base_url + '/api/metaModel/objectType', headers=headers, data=jdata)

    #def get_relationshipstypes(self, auth_key, base_ur):
        #pass

    #def get_atributestype(self, auth_key, base_ur):
        #pass

    #def get_atributes_assignment(self, auth_key, base_ur):
        #pass