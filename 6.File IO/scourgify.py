import sys
import csv

if len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')

table = []

try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = row['name'].rstrip().split(',')
            house = row['house']
            table.append([first.lstrip(), last, house])
except FileNotFoundError:
    sys.exit(f'Could not read {sys.argv[1]}')

with open(sys.argv[2], 'w') as file:
    writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
    writer.writerow({'first': 'first', 'last': 'last', 'house': 'house'})
    for row in table:
        writer.writerow({'first': row[0], 'last': row[1], 'house': row[2]})