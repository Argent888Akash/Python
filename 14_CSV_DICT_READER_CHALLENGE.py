import csv

countries_filename = 'country_info.txt'

countries = {}

with open(countries_filename, encoding='utf-8', newline='') as countries_file:
    reader = csv.DictReader(countries_file, delimiter='|')
    for row in reader:
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold()] = row

print(countries)
