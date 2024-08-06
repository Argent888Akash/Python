import csv

read_filename = 'cereal_grains.csv'
with open(read_filename, encoding='utf-8', newline='') as read_file:
    reader = csv.reader(read_file, quoting=csv.QUOTE_NONNUMERIC) # quoting converts all non-quoted (" ") fields to float
    for row in reader:                                           # csv had words in quotes and words non-quoted
        print(row)
