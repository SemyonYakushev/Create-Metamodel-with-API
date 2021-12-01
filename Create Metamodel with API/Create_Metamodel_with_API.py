from xml.etree import ElementTree
import requests
import base64
import json
import urllib3
import sys

auth_key = 'c3lzdGVtIGFkbWluaXN0cmF0b3I6MTIzcXdlQVNEKw=='
base_url = 'http://185.53.22.117:8008'
 
class APIGET:
    def get_objecttypes(self, auth_key, base_url):
        
        headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json', 
        'Authorization': 'Basic ' + auth_key,
        }

        response = requests.get(base_url + '/api/metaModel/objectType', headers=headers)
        items = json.loads(response.text)
        print(items)

    def get_relationshipstypes(rel_types, auth_key, base_ur):
    
        headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json', 
        'Authorization': 'Basic ' + auth_key,
        }

        response = requests.get(base_url + '/api/metaModel/relationshipTypes', headers=headers)
        items = json.loads(response.text)
        print(items)

    def get_relationships_pairs(self, auth_key, base_ur):
        pass

    def get_atributestype(self, auth_key, base_ur):
        pass

    def get_atributes_assignment(self, auth_key, base_ur):
        pass
