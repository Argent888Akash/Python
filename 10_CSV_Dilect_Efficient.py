import csv

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = ''
    for line in range(3):
        sample += countries_data.readline()
    country_dialect = csv.Sniffer().sniff(sample)  # sniff helps to identify different key things in sample data
    countries_data.seek(0)  # as sampling in line 6 - 8 reads 3 lines, .seek(0) bring curser to start

    reader = csv.reader(countries_data, dialect=country_dialect)  # dialect auto inputs delimiters, escape char etc
    for row in reader:                                            # dialect groups various csv setting together
        print(row)
