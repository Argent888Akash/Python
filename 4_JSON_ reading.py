import json
file_name = 'text.json'

with open(file_name, 'r', encoding='utf-8') as testfile:
    data = json.load(testfile)   # load method is used read json file

print(data)
print(data[2])
