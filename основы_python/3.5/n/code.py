import json


users = input()
updates = input()
json_file = {}

with open(users, 'rb') as file_in:
    users_json = json.loads(file_in.read())

for userdict in users_json:
    name = userdict['name']
    result = {}
    for key, val in userdict.items():
        if key != 'name':
            result.update({key: val})
    json_file.update({name: result})

with open(updates, 'rb') as file_in:
    updates_json = json.loads(file_in.read())

for userdict in updates_json:
    name = userdict['name']
    result = json_file.get(name)
    if not result:
        result = {}
    for key, val in userdict.items():
        if key != 'name':
            vals = [val]
            val_1 = result.get(key)
            if val_1:
                vals.append(val_1)
            result.update({key: max(vals)})
    json_file.update({name: result})

with open(users, "w", encoding="UTF-8") as file_out:
    json.dump(json_file, file_out, ensure_ascii=False, indent=4)
