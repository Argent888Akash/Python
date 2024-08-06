import  csv

cereals_filename = 'cereal_grains.csv'

with open(cereals_filename, 'r', encoding='utf-8', newline='') as cereals_file:
    reader = csv.DictReader(cereals_file)  # .DictReader() reads data as dictionary, makes 1st like as key
    for row in reader:
        print(row)
