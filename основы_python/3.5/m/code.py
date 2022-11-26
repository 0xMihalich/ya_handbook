from sys import stdin
import json


filename = input()
with open(filename, 'rb') as file_in:
    json_file = json.loads(file_in.read())

for line in stdin:
    key, value = line.replace('\n', '').split(' == ')
    json_file.update({key: value})

with open(filename, "w", encoding="UTF-8") as file_out:
    json.dump(json_file, file_out, ensure_ascii=False, indent=4)
