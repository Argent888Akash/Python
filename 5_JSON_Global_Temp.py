import json

file_name = ('data.json')


with open(file_name, encoding='utf-8') as data:
    anomalies = json.load(data)

print(anomalies['description'])
# print(anomalies['data'])
for year, values in anomalies['data'].items():
    year, values = int(year), float(values)
    print(year, values)
