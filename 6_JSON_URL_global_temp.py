import json
import urllib.request

file_name = ('https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/6/1850-2024/data.json')


with urllib.request.urlopen(file_name) as json_stream:  # opening url

    data = json_stream.read().decode('utf-8')   # reading and decoding data from url
    anomalies = json.loads(data)    # .load is used for file, .loads is used for url

print(anomalies['description'])
# print(anomalies['data'])
for year, values in anomalies['data'].items():
    year, values = int(year), float(values)
    print(year, values)
