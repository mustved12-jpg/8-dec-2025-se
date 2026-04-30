import json
data=''
with open('json 1.json','r') as f:
    data=json.load(f)
print(data)
print(data['name'])
