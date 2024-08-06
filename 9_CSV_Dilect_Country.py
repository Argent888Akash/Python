import csv

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = countries_data.read()
    country_dialect = csv.Sniffer().sniff(sample)  # sniff helps to identify different key things in sample data
    countries_data.seek(0)  # as .read() on line 6 reads all lines, .seek(0) bring curser to start

    reader = csv.reader(countries_data, dialect=country_dialect)  # dialect auto inputs delimiters, etc
    for row in reader:
        print(row)
