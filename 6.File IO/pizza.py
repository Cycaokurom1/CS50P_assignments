import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')
elif len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif not sys.argv[1].endswith('csv'):
    sys.exit('Not a CSV file')

table = []

try:
    with open(sys.argv[1]) as file:
        for line in file:
            pizza, small, large = line.rstrip().split(',')
            table.append([pizza, small, large])
        print(tabulate(table, headers='firstrow', tablefmt='grid'))
except FileNotFoundError:
    sys.exit('File does not exist')