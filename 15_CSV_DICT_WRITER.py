import csv

countries_filename = 'country_info.txt'

dialect = csv.excel    # adding .excel dialect, imports attributes of .excel, but we change delimiter in next line
dialect.delimiter = '|'

countries = {}

with open(countries_filename, encoding='utf-8', newline='') as countries_file:

    headings = countries_file.readline().strip().split(dialect.delimiter)  # get column headings from first line

    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()  # replacing proper case headings to lowercase
        # and providing head heading in the next line

    reader = csv.DictReader(countries_file, dialect=dialect, fieldnames=headings)  # fieldnames provides headings
    for row in reader:
        countries[row['country'].casefold()] = row
        countries[row['cc'].casefold()] = row

print(countries)
