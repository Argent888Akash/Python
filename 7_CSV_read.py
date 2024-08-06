import csv

csv_filename = 'OlympicMedals_2020.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file: # newline='' is a good practice suggested in csv module
    headers = csv_file.readline().strip().split(',')
    print(f'Column headers: {headers}')
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
