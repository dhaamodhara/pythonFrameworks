import json
data={"user": "dhamodhara", "password":"123", "hi":None}
with open("new_data.json", "w") as f:
    result=json.dumps(data)
    print(result)
    print(type(result))
with open("new_data.json", 'r') as f:
    re=json.loads(result)
    print(re)
    print(type(re))
