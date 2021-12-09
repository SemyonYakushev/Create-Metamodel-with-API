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

    def post_relationshiptypes(auth_key, base_url, file):
        columns = ['RelationTypeName', 'FromObjectTypeName', 'ToObjectTypeName']
        relations = pd.read_excel(io=file, header = 0, engine='openpyxl', sheet_name = "Mapping")
        headers = {
                'Accept': 'application/json',
                'Content-Type': 'application/json', 
                'Authorization': 'Basic ' + auth_key
                }
        rel_json = {}
        relType = ""
        for index, item in relations.iterrows():
            if relType != item['RelationTypeName']:
                if len(rel_json) > 0:
                     jdata = json.dumps(rel_json)
                     response = requests.post(base_url + '/api/metaModel/relationshipType', headers=headers, data=jdata)
                     print(rel_json)
                     print('------------------------------------------')
                rel_json = {'Name': item['RelationTypeName'],
                        'Rules': [
                            {
                            'SourceType': {'Type': item['FromObjectTypeName']},
                            'TargetType': {'Type': item['ToObjectTypeName']}
                            }
                            ],
                            'SourceToTargetDescription': item['SourceToTarget'], 
                            'TargetToSourceDescription': item['TargetToSource'],
                            'HasDirection': 'true'
                            }
                relType = item['RelationTypeName']
               
            else:
                rel_json['Rules'].append(
                            {
                            'SourceType': {'Type': item['FromObjectTypeName']},
                            'TargetType': {'Type': item['ToObjectTypeName']}
                            })
               
        jdata = json.dumps(rel_json)
        response = requests.post(base_url + '/api/metaModel/relationshipType', headers=headers, data=jdata)


            

    def post_attributetypes(auth_key, base_url, file):
         


       attributes = pd.read_excel(io=file, header = 0, engine='openpyxl', sheet_name = "Attribute") 
       headers = {
           'Accept': 'application/json',
           'Content-Type': 'application/json', 
           'Authorization': 'Basic ' + auth_key
           }

       for index, item in attributes.iterrows():
          atr_json = {
          'Name': item['RusAttrName'],
          'DataType':  item['AttributeType'],
          'IsMandatory': 'false',
          'SyncWithVisio': item['IsSynchronised'],
          'VisioSyncName': item['VisioSyncName'],
          'RowHeight': item['TextRowCount'],
          'ListValues': []
          }
          if item['AttributeType'] == 'List':
              xmlvalue = ElementTree.fromstring(item['ListValues'])
              for a in xmlvalue:
                atr_json['ListValues'].append(
                {
                'Name': a.text
                })
      
          jdata = json.dumps(atr_json)
          response = requests.post(base_url + '/api/metaModel/attributeType', headers=headers, data=jdata)
          print(atr_json)

    def post_atributes_assignment(auth_key, base_url, file):

        assignments = pd.read_excel(io=file, header = 0, engine='openpyxl', sheet_name = "AttrGrouping")

        headers = {
           'Accept': 'application/json',
           'Content-Type': 'application/json', 
           'Authorization': 'Basic ' + auth_key
           }
        
        asm_json = {}
        atrType = ""
        atrGroup = ""
        group_json = {}
        for index, item in assignments.iterrows():
            if atrType != item['ObjectTypeName']:

                if len(asm_json)>0:
                    asm_json['Tabs'].append(group_json)
                    group_json = {}
                    jdata = json.dumps(asm_json)
                    response = requests.post(base_url + '/api/metaModel/attributes', headers=headers, data=jdata)
                    print(asm_json['Name'])
                    if response.status_code != 201:
                       print(asm_json['Name'])
                       print(asm_json)
                       print(response.status_code)
                       print(response.text)
                asm_json = {   
                    'GeneralType': 'Object',
                    'Name': item['ObjectTypeName'],
                    'Tabs': []
                    }
                atrGroup = ""
                atrType = item['ObjectTypeName']
            if atrGroup != item['AttributeGroupName']:
                if len(group_json)>0:
                    asm_json['Tabs'].append(group_json)
                group_json = {}
                group_json['Name'] = item['AttributeGroupName']
                group_json['AttributeNames'] = []
                atrGroup = item['AttributeGroupName']
            group_json['AttributeNames'].append(item['AttrName'])
          

        
        
           


iServerMetamodel.post_objecttypes(auth_key = auth_key, base_url = base_url, file=file)
iServerMetamodel.post_relationshiptypes(auth_key = auth_key, base_url = base_url, file=file)
iServerMetamodel.post_attributetypes(auth_key = auth_key, base_url = base_url, file=file)
iServerMetamodel.post_atributes_assignment(auth_key = auth_key, base_url = base_url, file=file)