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

class iServerMetamodel:
    def post_objecttypes(auth_key, base_url, file):
       objects = pd.read_excel(io=file, header = 0, engine='openpyxl', sheet_name = "ObjectTypes") 
       headers = {
           'Accept': 'application/json',
           'Content-Type': 'application/json', 
           'Authorization': 'Basic ' + auth_key
           }
 
       for index, item in objects.iterrows():
           obj_json = {'Name': item['RusTypeName'], 'Description': item['ObjectTypeName']}
           jdata = json.dumps(obj_json)
           response = requests.post(base_url + '/api/metaModel/objectType', headers=headers, data=jdata)
           print(response.text)

    def post_relationshipstypes(auth_key, base_url, file):
        columns = ['RelationTypeName', 'FromObjectTypeName', 'ToObjectTypeName']
        relations = pd.read_excel(io=file, header = 0, engine='openpyxl', sheet_name = "Mapping")
        headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json', 
                'Authorization': 'Basic ' + auth_key
                }

        for index, item in relations.iterrows():
            rel_json = {'Name': item['RelationTypeName'],
                        'Rules': [
                            {'SourceType': {'Type': item['FromObjectTypeName']},
                            'TargetType': {'Type': item['ToObjectTypeName']}}], 'SourceToTargetDescription': item['SourceToTarget'], 'TargetToSourceDescription': item['TargetToSource']}    
            jdata = json.dumps(rel_json)
            response = requests.post(base_url + '/api/metaModel/relationshipType', headers=headers, data=jdata)
            print(response.text)

    #def get_atributestype(self, auth_key, base_url):
        #pass

    #def get_atributes_assignment(self, auth_key, base_url):
        #pass


iServerMetamodel.post_objecttypes(auth_key = auth_key, base_url = base_url, file=file)